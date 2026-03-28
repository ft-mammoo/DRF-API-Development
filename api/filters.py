import django_filters
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    emp_id_min = django_filters.CharFilter(method='filter_emp_id', label='From Emp_id')
    emp_id_max = django_filters.CharFilter(method='filter_emp_id', label='To Emp_id')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    class Meta:
        model = Employee
        fields = ['emp_id_min', 'emp_id_max', 'emp_name', 'designation']

    def filter_emp_id(self, queryset, name, value):
        if name == 'emp_id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'emp_id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset.filter(emp_id=value)