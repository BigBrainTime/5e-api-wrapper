import httpx
import warnings
import json

API = 'https://www.dnd5eapi.co/api/'

class APICall():
    async def __init__(self, top_level: str = '', specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes APICall with top level and specific endpoints.
    
        Parameters:
        - top_level (str): Top level endpoint, empty string for base API url 
        - specific (str): Specific endpoint 
        - items_per_page (int): Number of items per page for pagination
        
        Sets attributes:
        - response: API response 
        - status: response status code
        - data: JSON response data
        - pages: paginated results 
        - results: API results
        - count: number of results
        
        Handles API errors and pagination.
        """
        if top_level == '':
            self.response = await httpx.get(f'{API}')
        else:
            self.response = await httpx.get(f'{API}/{top_level}/{specific}')
        self.status = self.response.status_code
        self.data = json.loads(self.response.text)

        self.pages = []

        if self.status not in (200,404):
            self.results = []
            self.count = 0
            warnings.warn('Invalid response from API')
        
        elif self.status == 404:
            self.results = self.data
            self.count = 0

        elif top_level == '':
            self.count = len(self.data)
            self.results = self.data
            if itemes_per_page is not None:
                self.paginate_results(len(self.results))
            else:
                self.pages = self.results if isinstance(self.results, list) else [self.results]

        elif specific == '':
            self.count = self.data['count']
            self.results = self.data['results']
            if itemes_per_page is not None:
                self.paginate_results(len(self.results))
            else:
                self.pages = self.results if isinstance(self.results, list) else [self.results]

        else:
            self.count = 1
            self.results = self.data
            if itemes_per_page is not None:
                self.paginate_results(len(self.results))
            else:
                self.pages = self.results if isinstance(self.results, list) else [self.results]

    def paginate_results(self, items_per_page: int):
        """Paginates the results into pages of items_per_page items each.
    
        Iterates through the results and appends pages of items_per_page items to 
        the self.pages list. Any remaining items are added as a final partial page.
        """
        self.pages=[]
        new_page = []
        for page in self.results:
            if len(new_page) >= items_per_page:
                self.pages.append(new_page)
                new_page = []

            new_page.append(page)

        if len(new_page) > 0:
            self.pages.append(new_page)

    def __str__(self) -> str:
        data = {
            "status":self.status,
            "count":self.count,
            "results":self.results
        }
        return json.dumps(data)
    

class AbilityScores(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes an AbilityScores API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('ability-scores', specific, itemes_per_page)


class Alignments(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes an Alignments API call.

        Args:
        specific (str): Optional filter to get a specific alignment by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('alignments', specific, itemes_per_page)


class Backgrounds(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Backgrounds API call.

        Args:
        specific (str): Optional filter to get a specific background by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('backgrounds', specific, itemes_per_page)


class Classes(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Classes API call.

        Args:
        specific (str): Optional filter to get a specific class by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('classes', specific, itemes_per_page)


class Conditions(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Conditions API call.

        Args:
        specific (str): Optional filter to get a specific condition by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('conditions', specific, itemes_per_page)


class DamageTypes(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a DamageTypes API call.

        Args:
        specific (str): Optional filter to get a specific damage type by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('damage-types', specific, itemes_per_page)


class Equipment(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Equipment API call.

        Args:
        specific (str): Optional filter to get a specific equipment by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('equipment', specific, itemes_per_page)


class EquipmentCategories(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes an EquipmentCategories API call.

        Args:
        specific (str): Optional filter to get a specific equipment category by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('equipment-categories', specific, itemes_per_page)


class Feats(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Feats API call.

        Args:
        specific (str): Optional filter to get a specific feat by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('feats', specific, itemes_per_page)


class Features(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Features API call.

        Args:
        specific (str): Optional filter to get a specific features by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('features', specific, itemes_per_page)


class Languages(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Languages API call.

        Args:
        specific (str): Optional filter to get a specific language by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('languages', specific, itemes_per_page)


class MagicItems(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a MagicItems API call.

        Args:
        specific (str): Optional filter to get a specific magic item by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('magic-items', specific, itemes_per_page)


class MagicSchools(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a MagicSchools API call.

        Args:
        specific (str): Optional filter to get a specific magic school by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('magic-schools', specific, itemes_per_page)


class Monsters(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Monsters API call.

        Args:
        specific (str): Optional filter to get a specific monster by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('monsters', specific, itemes_per_page)


class Proficiencies(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Proficiencies API call.

        Args:
        specific (str): Optional filter to get a specific proficiency by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('proficiencies', specific, itemes_per_page)


class Races(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Races API call.

        Args:
        specific (str): Optional filter to get a specific race by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('races', specific, itemes_per_page)


class Rules(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Rules API call.

        Args:
        specific (str): Optional filter to get a specific rule by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('rules', specific, itemes_per_page)


class Skills(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Skills API call.

        Args:
        specific (str): Optional filter to get a specific skill by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('skills', specific, itemes_per_page)


class Spells(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Spells API call.

        Args:
        specific (str): Optional filter to get a specific spell by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('spells', specific, itemes_per_page)


class Subclasses(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Subclasses API call.

        Args:
        specific (str): Optional filter to get a specific subclass by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('subclasses', specific, itemes_per_page)


class Subraces(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Subraces API call.

        Args:
        specific (str): Optional filter to get a specific subrace by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('subraces', specific, itemes_per_page)


class Traits(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Traits API call.

        Args:
        specific (str): Optional filter to get a specific trait by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('traits', specific, itemes_per_page)


class WeaponProperties(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a WeaponProperties API call.

        Args:
        specific (str): Optional filter to get a specific weapon property by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('weapon-properties', specific, itemes_per_page)