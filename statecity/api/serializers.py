from rest_framework import serializers
from statecity.models import City, StateSubsidy

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name']

class StateSubsidySerializer(serializers.ModelSerializer):
    class Meta:
        model = StateSubsidy
        fields = ['id', 'state', 'city', 'subsidy_rate', 'state_generation']

# class DistrictGroupBySerializer(serializers.ModelSerializer):
#     city = serializers.SerializerMethodField()
#     state_name = serializers.ReadOnlyField(source='state')  # assuming 'state' is a string, not a foreign key

#     class Meta:
#         model = StateSubsidy
#         fields = ['state_name', 'id', 'average_generation_per_kwp', 'subsidy_rate', 'city']

#     def get_city(self, obj):
#         # Assuming obj.city is an instance of the City model, and you want to return its details
#         if obj.city:
#             return {'id': obj.city.id, 'city_name': obj.city.city_name}
#         return None
