from django.contrib.auth.mixins import AccessMixin


class JournalOwnerRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)