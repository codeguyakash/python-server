from rest_framework import serializers
from Solar.models import SolarCalculator, City, StateSubsidy
from statecity.api.serializers import CitySerializer, StateSubsidySerializer



class SolarCalculatorSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), source='city', write_only=True)
    state = StateSubsidySerializer(read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(
        queryset=StateSubsidy.objects.all(), source='state', write_only=True)

    recommended_system_size = serializers.SerializerMethodField()
    total_installation_cost = serializers.SerializerMethodField()
    saving_in_25_years = serializers.SerializerMethodField()
    annual_return_on_investment = serializers.SerializerMethodField()
    investment_payback_period = serializers.SerializerMethodField()
    monthly_electricity_production = serializers.SerializerMethodField()
    monthly_cost_saving = serializers.SerializerMethodField()
    loan_amount = serializers.SerializerMethodField()
    down_payment = serializers.SerializerMethodField()
    subsidy_amount = serializers.SerializerMethodField()
    subsidy_upto_2kw = serializers.SerializerMethodField()
    subsidy_upto_3kw = serializers.SerializerMethodField()
    with_subsidy = serializers.SerializerMethodField()
    emi_amount = serializers.SerializerMethodField()
    area_requirement_in_sqft = serializers.SerializerMethodField()
    system_size_requirement_if_load_details = serializers.SerializerMethodField()

    class Meta:
        model = SolarCalculator
        fields = ['id', 'state', 'state_id', 'city', 'city_id', 'monthly_average_consumption', 
                  'load_requirement', 'roof_area', 
                  'average_rate_per_unit', 'margin_money_percentage', 
                  'interest_rate', 'loan_period', 'recommended_system_size', 
                  'total_installation_cost', 'saving_in_25_years', 'annual_return_on_investment', 
                  'investment_payback_period', 'monthly_electricity_production', 
                  'monthly_cost_saving', 'loan_amount', 'down_payment', 'subsidy_amount',
                  'subsidy_upto_2kw', 'subsidy_upto_3kw', 'with_subsidy', 'emi_amount',
                  'area_requirement_in_sqft', 'system_size_requirement_if_load_details']
        read_only_fields = [  
                            'recommended_system_size', 'total_installation_cost', 'saving_in_25_years', 
                            'annual_return_on_investment', 'investment_payback_period', 
                            'monthly_electricity_production', 'monthly_cost_saving', 'loan_amount', 
                            'down_payment', 'subsidy_amount', 'subsidy_upto_2kw', 'subsidy_upto_3kw',
                            'with_subsidy', 'emi_amount', 'area_requirement_in_sqft', 
                            'system_size_requirement_if_load_details','state_generation']

    def get_recommended_system_size(self, obj):
        return round(obj.recommended_system_size(), 2)

    def get_total_installation_cost(self, obj):
        return round(obj.cost_without_subsidy(), 2)

    def get_saving_in_25_years(self, obj):
        return round(obj.saving_in_25_years(), 2)

    def get_annual_return_on_investment(self, obj):
        return round(obj.annual_return_on_investment(), 2)

    def get_investment_payback_period(self, obj):
        return round(obj.investment_payback_period(), 2)

    def get_monthly_electricity_production(self, obj):
        return round(obj.monthly_electricity_production(), 2)

    def get_monthly_cost_saving(self, obj):
        return round(obj.monthly_cost_saving(), 2)

    def get_loan_amount(self, obj):
        return round(obj.loan_amount(), 2)

    def get_down_payment(self, obj):
        return round(obj.down_payment(), 2)

    def get_subsidy_amount(self, obj):
        return round(obj.subsidy_amount(), 2)

    def get_subsidy_upto_2kw(self, obj):
        return round(obj.subsidy_upto_2kw(), 2)

    def get_subsidy_upto_3kw(self, obj):
        return round(obj.subsidy_upto_3kw(), 2)

    def get_with_subsidy(self, obj):
        return round(obj.cost_with_subsidy(), 2)

    def get_emi_amount(self, obj):
        return round(obj.emi_amount(), 2)

    def get_area_requirement_in_sqft(self, obj):
        return round(obj.area_requirement_in_sqft(), 2)

    def get_system_size_requirement_if_load_details(self, obj):
        return round(obj.system_size_requirement(), 2)
