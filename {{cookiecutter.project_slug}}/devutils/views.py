from rest_framework import mixins, status, response


class RestrictedListViewMixin(mixins.ListModelMixin):
    """
        The inheriting view must implement "restriction_fields" attribute,
        this mixin will not allow the list method to be executed
        unless the specified filters are present in url
    """
    restriction_fields = []

    def list(self, request, *args, **kwargs):
        if self.restriction_fields and set(
                self.restriction_fields).issubset(set(request.GET.keys())):
            return super().list(request, *args, **kwargs)
        else:
            return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class OptionalPaginateMixin:
    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class ActionBasedSerializerMixin:
    """
    ---
    # Specify Different Serializers for actions
    """
    # serializer_class_by_action = {}

    def get_serializer_class(self):
        if hasattr(self, 'serializer_class_by_action'):
            return self.serializer_class_by_action.get(self.action, self.serializer_class)
        return super().get_serializer_class()
