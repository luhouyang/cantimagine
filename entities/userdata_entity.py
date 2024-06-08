class UserdataEntity:
    def __init__(self, name_of_company="", offering="", audience="", problem_solved="",
                 technologies="", area_of_operation="", market="", value="",
                 competitor1="", competitor2="", key_difference="", state_of_startup="",
                 resources_asked="", how_resources_used="", chat_history=None,
                 pitch="", blobs_urls=None):
        self.name_of_company = name_of_company
        self.offering = offering
        self.audience = audience
        self.problem_solved = problem_solved
        self.technologies = technologies
        self.area_of_operation = area_of_operation
        self.market = market
        self.value = value
        self.competitor1 = competitor1
        self.competitor2 = competitor2
        self.key_difference = key_difference
        self.state_of_startup = state_of_startup
        self.resources_asked = resources_asked
        self.how_resources_used = how_resources_used
        self.chat_history = chat_history if chat_history else []
        self.pitch = pitch
        self.blobs_urls = blobs_urls if blobs_urls else []