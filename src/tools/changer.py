from src.models import Lead


class Changer:
    @staticmethod
    def change_lead_name(lead: Lead, new_name: str) -> None:
        lead.name = new_name
