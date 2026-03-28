import django_filters
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    emp_id_min = django_filters.CharFilter(field_name='emp_id', lookup_expr='gte')
    emp_id_max = django_filters.CharFilter(field_name='emp_id', lookup_expr='lte')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['emp_name', 'designation']
