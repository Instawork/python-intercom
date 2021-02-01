from intercom import team
from intercom.api_operations.all import All
from intercom.service.base_service import BaseService


class Team(BaseService, All):

    @property
    def collection_class(self):
        return team.Team
