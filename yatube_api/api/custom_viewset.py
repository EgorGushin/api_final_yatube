from rest_framework import mixins, viewsets


class FollowCreatListViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    pass
