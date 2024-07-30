from rest_framework import serializers
from statecity.models import *
from contact.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction


class SolarInquirySerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), write_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)
    state = serializers.PrimaryKeyRelatedField(queryset=StateSubsidy.objects.all(), write_only=True)
    state_name = serializers.CharField(source='state.state', read_only=True)
    

    class Meta:
        model = SolarInquiry
        fields = [
            'id', 'city', 'interest_in', 'name', 'contract_number', 'company_name', 
            'email', 'state', 'city', 'city_name', 'state_name', 'pin_code', 'address', 'comments'
        ]
        
    def create(self, validated_data):
        with transaction.atomic():
            city_location = validated_data.pop('city', None)
            state_subsidy = validated_data.pop('state', None)

        if city_location:
            validated_data['city'] = city_location
        if state_subsidy:
            validated_data['state'] = state_subsidy

        inquiry = SolarInquiry.objects.create(**validated_data)
        SolarStatus.objects.create(solar_inquiry=inquiry)

        user = self.context['request'].user
        if user.is_authenticated and hasattr(user, 'is_channel_partner') and user.is_channel_partner:
            inquiry.distributor = user
            inquiry.save()
            self.send_distributor_email(user.email, user.username, validated_data)

        return inquiry  

    
    
    
    
    
    
    def send_distributor_email(self, distributor_email, distributor_name, inquiry_data):
        subject = f"New Solar Inquiry Submitted"
        message = f"""
        Dear {distributor_name},

        You have received a new solar inquiry.

        Details:
        Name: {inquiry_data.get('name')}
        Email: {inquiry_data.get('email')}
        Phone: {inquiry_data.get('contract_number')}
        Address: {inquiry_data.get('address')}
        Comments: {inquiry_data.get('comments')}

        Please follow up with the customer at your earliest convenience.

        Best regards,
        Solar Inquiry Team
        """

        print(f"Attempting to send email to: {distributor_email} with subject: {subject}")
        try:
            result = send_mail(
                subject,
                message,
                'no-reply@solar.com',
                [distributor_email],
                fail_silently=False,
            )
            print(f"Email send result: {result}")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")



        
        
        

class SolarStatusSerializer(serializers.ModelSerializer):
    solar_inquiry_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(source='solar_inquiry.name', read_only=True)
    pincode = serializers.CharField(source='solar_inquiry.pin_code', read_only=True)
    comment = serializers.CharField(source='solar_inquiry.comments', read_only=True)
    address = serializers.CharField(source='solar_inquiry.address', read_only=True)
    email = serializers.SerializerMethodField()

    class Meta:
        model = SolarStatus
        fields = [
            'solar_inquiry_id', 'order_status', 'site_survey_status', 'installation_status',
            'grid_connectivity_status', 'name', 'pincode', 'comment', 'address', 'email'
        ]
        read_only_fields = ['name', 'pincode', 'comment', 'address', 'email']  # Ensure 'solar_inquiry_id' is not here

    def get_email(self, obj):
        return obj.solar_inquiry.email if obj.solar_inquiry else 'No email available'

    def create(self, validated_data):
        solar_inquiry_id = validated_data.pop('solar_inquiry_id', None)
        solar_inquiry = None
        if solar_inquiry_id:
            try:
                solar_inquiry = SolarInquiry.objects.get(id=solar_inquiry_id)
            except SolarInquiry.DoesNotExist:
                raise serializers.ValidationError({"solar_inquiry_id": "No Solar Inquiry found with this ID."})
            validated_data['solar_inquiry'] = solar_inquiry

        status_instance, created = SolarStatus.objects.update_or_create(
            solar_inquiry=solar_inquiry,
            defaults=validated_data
        )
        return status_instance

    
    
    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     print("Debug instance:", instance)  # Debug print
    #     if hasattr(instance, 'solar_inquiry') and instance.solar_inquiry:
    #         ret['email'] = instance.solar_inquiry.email
    #         print("Debug email:", instance.solar_inquiry.email)  # Debug print
    #     else:
    #         ret['email'] = 'No email available'
    #         print("Debug email not available")  # Debug print
    #     return ret


    
    
    def update(self, instance, validated_data):
        instance.order_status = validated_data.get('order_status', instance.order_status)
        instance.site_survey_status = validated_data.get('site_survey_status', instance.site_survey_status)
        instance.installation_status = validated_data.get('installation_status', instance.installation_status)
        instance.grid_connectivity_status = validated_data.get('grid_connectivity_status', instance.grid_connectivity_status)
        instance.save()
        return instance
            
            
class SolarMaintanceSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), write_only=True)
    city_name = serializers.CharField(source='city.name', read_only=True)
    state = serializers.PrimaryKeyRelatedField(queryset=StateSubsidy.objects.all(), write_only=True)
    state_name = serializers.CharField(source='state.state', read_only=True)

    class Meta:
        model = SolarMaintanceInquries
        fields = [
            'id', 'city', 'interest_in', 'name', 'contract_number', 'company_name', 
            'email', 'state', 'city_name', 'state_name', 'pin_code', 'address', 'comments'
        ]
    def validate_state(self, value):
        if not value:
            raise serializers.ValidationError("This field cannot be blank.")
        return value    
        
    # def validate_city(self, value):
    #     if not isinstance(value, int):
    #         raise serializers.ValidationError("City ID must be an integer")
    #     return value

    # def validate_state(self, value):
    #     if not isinstance(value, int):
    #         raise serializers.ValidationError("State ID must be an integer")
    #     return value
    

    def create(self, validated_data):
        # No need to manually set city and state, they are handled by DRF
        with transaction.atomic():
            inquiry = SolarMaintanceInquries.objects.create(**validated_data)
            SolarMaintainceStatus.objects.create(solar_inquiry=inquiry)

            user = self.context['request'].user
            if hasattr(user, 'is_channel_partner') and user.is_channel_partner:
                inquiry.distributor = user
                inquiry.save()
                self.send_distributor_email(user.email, user.username, validated_data)

        return inquiry    
    
    def send_distributor_email(self, distributor_email, distributor_name, inquiry_data):
        subject = f"New Solar Inquiry Submitted"
        message = f"""
        Dear {distributor_name},

        You have received a new solar Maintaince inquiry.

        Details:
        Name: {inquiry_data.get('name')}
        Email: {inquiry_data.get('email')}
        Phone: {inquiry_data.get('contract_number')}
        Address: {inquiry_data.get('address')}
        Comments: {inquiry_data.get('comments')}

        Please follow up with the customer at your earliest convenience.

        Best regards,
        Solar Inquiry Team
        """

        send_mail(
            subject,
            message,
            'no-reply@solar.com',
            [distributor_email],
            fail_silently=False,
        )



class SolarStatusMaintanceSerializer(serializers.ModelSerializer):
    solar_inquiry_id = serializers.IntegerField(read_only=True)  
    name = serializers.CharField(source='solar_inquiry.name', read_only=True)
    pincode = serializers.CharField(source='solar_inquiry.pin_code', read_only=True)
    comment = serializers.CharField(source='solar_inquiry.comments', read_only=True)
    email = serializers.SerializerMethodField()  

    class Meta:
        model = SolarMaintainceStatus
        fields = [
            'solar_inquiry_id', 'request_status', 'Technician_status', 'service_status',
            'solar_inquiry', 'name', 'pincode', 'comment', 'email'
        ]
        read_only_fields = ['solar_inquiry', 'name', 'pincode', 'comment', 'email']

    def get_email(self, obj):
        return obj.solar_inquiry.email if obj.solar_inquiry else 'No email available'

    def create(self, validated_data):
        solar_inquiry_id = validated_data.pop('solar_inquiry_id', None)
        solar_inquiry = None
        if solar_inquiry_id:
            try:
                solar_inquiry = SolarInquiry.objects.get(id=solar_inquiry_id)
            except SolarInquiry.DoesNotExist:
                raise serializers.ValidationError({"solar_inquiry_id": "No Solar Inquiry found with this ID."})
            validated_data['solar_inquiry'] = solar_inquiry

        maintaince_status_instance, created = SolarMaintainceStatus.objects.update_or_create(
            solar_inquiry=solar_inquiry,
            defaults=validated_data
        )
        return maintaince_status_instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['email'] = instance.solar_inquiry.email if instance.solar_inquiry else 'No email available'
        return ret

    

        
    #admin123456,u=db@12gmail.com