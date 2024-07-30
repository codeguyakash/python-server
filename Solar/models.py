from django.db import models
import math
from statecity.models import StateSubsidy,City
from math import ceil


# class Appliance(models.Model):
#     name = models.CharField(max_length=100)
#     load_watts = models.FloatField(help_text="Load of the appliance in watts")
#     average_hours_per_day = models.FloatField(default=4, help_text="Average hours per day the appliance is used")


class SolarCalculator(models.Model):
    state = models.ForeignKey(StateSubsidy, on_delete=models.SET_NULL, null=True, help_text="Select the state")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, help_text="Select the city")
    monthly_average_consumption = models.IntegerField(help_text="Monthly average electricity consumption (units)", default=None, null=True)
    load_requirement = models.FloatField(help_text="Load requirement (kW)", default=0.0)
    roof_area = models.FloatField(help_text="Roof area in square feet", default=0.0)
    state_generation = models.FloatField(help_text="Generation rate per state", default=None, null=True)
    average_rate_per_unit = models.FloatField(help_text="Average rate of electricity per unit/kWh", default=None, null=True)
    
    margin_money_percentage = models.FloatField(default=20.0, help_text="Margin Money (Minimum 20%)", null=True)
    interest_rate = models.FloatField(default=8.9, help_text="Rate of interest (%)", null=True)
    loan_period = models.IntegerField(default=10, help_text="Loan period in years", null=True)
    
    
    def save(self, *args, **kwargs):
        if not self.state_generation:
            try:
                state_subsidy = StateSubsidy.objects.get(state=self.state.state, city=self.city)
                self.state_generation = state_subsidy.state_generation
            except StateSubsidy.DoesNotExist:
                self.state_generation = 0  
        super(SolarCalculator, self).save(*args, **kwargs)


    def system_size_requirement(self):
        if self.monthly_average_consumption and self.state_generation:
            return math.ceil(self.monthly_average_consumption / (self.state_generation * 30))
        elif self.load_requirement:
            return max(self.load_requirement, 0)
        return 0

    def recommended_system_size(self):
        size_required = self.system_size_requirement()
        if size_required:
            return max(math.ceil(size_required / 0.55) * 0.55, 0)   #dynamic c55
        return 0

    def area_requirement_in_sqft(self):
        return self.recommended_system_size() * 75

    def cost_without_subsidy(self):      # dyanamic 
        return 60000 * self.recommended_system_size()

    def subsidy_upto_2kw(self):
        size = self.recommended_system_size()
        if size > 2:
            return 60000    # dynamic
        return size * 30000

    def subsidy_upto_3kw(self):
        size = self.recommended_system_size()
        if 2 < size <= 3:
            return (size - 2) * 8000
        return 0

    def subsidy_amount(self):
        return min(self.subsidy_upto_2kw() + self.subsidy_upto_3kw(), 78000)  # dynamic 

    def cost_with_subsidy(self):
        return self.cost_without_subsidy() - self.subsidy_amount()

    def down_payment(self):
        if self.cost_with_subsidy() and self.margin_money_percentage is not None:
            return self.cost_with_subsidy() * (self.margin_money_percentage / 100)
        return 0

    def loan_amount(self):
        if self.cost_with_subsidy() and self.down_payment() is not None:
            return self.cost_with_subsidy() - self.down_payment()
        return 0

    def monthly_electricity_production(self):
        if self.recommended_system_size() and self.state_generation:
            return self.recommended_system_size() * self.state_generation * 30
        return 0

    def monthly_cost_saving(self):
        if self.monthly_electricity_production() and self.average_rate_per_unit:
            return self.monthly_electricity_production() * self.average_rate_per_unit
        return 0

    def investment_payback_period(self):
        monthly_saving = self.monthly_cost_saving()
        if monthly_saving > 0:
            return self.subsidy_amount() / (monthly_saving * 12)
        return 0
    
    


    def saving_in_25_years(self):
        return self.monthly_cost_saving() * 12 * 25

    def annual_return_on_investment(self):
        cost_with_subsidy = self.cost_with_subsidy()
        if cost_with_subsidy > 0:
            return self.saving_in_25_years() / cost_with_subsidy / 25 * 0.8
        return 0

    def emi_amount(self):
        if self.loan_amount() and self.loan_period and self.interest_rate:
            rate_per_month = self.interest_rate / (12 * 100)
            numerator = rate_per_month * ((1 + rate_per_month) ** (self.loan_period * 12))
            denominator = ((1 + rate_per_month) ** (self.loan_period * 12)) - 1
            return self.loan_amount() * numerator / denominator
        return 0
    
    
    
    # @property
    # def total_daily_consumption(self):
    #     return sum([usage.units_per_day for usage in self.applianceusage_set.all()])

    # @property
    # def total_monthly_consumption(self):
    #     return self.total_daily_consumption * 30

    # @property
    # def capacity_requirement(self):
    #     return self.total_daily_consumption / 4

    # @property
    # def max_load(self):
    #     return ceil(sum([usage.load for usage in self.applianceusage_set.all()]) / 1000)

    # @property
    # def requirement(self):
    #     return self.max_load * 0.8

# class ApplianceUsage(models.Model):
#     calculator = models.ForeignKey(SolarCalculator, on_delete=models.CASCADE)
#     appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
#     number_of_equipments = models.IntegerField(default=1)

#     @property
#     def units_per_day(self):
#         return self.appliance.load_watts * self.number_of_equipments * self.appliance.average_hours_per_day / 1000

#     @property
#     def load(self):
#         return self.appliance.load_watts * self.number_of_equipments