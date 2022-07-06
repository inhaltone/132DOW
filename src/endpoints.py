from enum import Enum


class Endpoints(Enum):
    THE_GUARDIAN_DISCUSSION_API = 'https://discussion.theguardian.com/discussion-api/discussion'
    THE_GUARDIAN_UKRAINE = 'https://www.theguardian.com/world/ukraine/2022/feb/23/all'
    THE_GUARDIAN_RUSSIA = 'https://www.theguardian.com/world/russia/2022/feb/23/all'
    THE_GUARDIAN_NATO = 'https://www.theguardian.com/world/nato/2022/feb/23/all'
    THE_GUARDIAN_PUTIN = 'https://www.theguardian.com/world/vladimir-putin/2022/feb/23/all'
    KATHIMERINI_TAGS_POLEMOS_STIN_OUKRANIA = 'https://www.kathimerini.gr/tag/polemos-stin-oykrania/'
    NAFTEMPORIKI_POLEMOS_STIN_OUKRANIA = 'https://www.naftemporiki.gr/stream/3137/polemos-stin-oukrania'
    NAFTEMPORIKI_BASE_URL = 'https://www.naftemporiki.gr/'
    EFSYN_BASE_URL = 'https://www.efsyn.gr'
    EFSYN_OUKRANIA = 'https://www.efsyn.gr/oykrania'


class Hashtags(Enum):
    UKRAINE = '#Ukraine'
    RUSSIA_IS_A_TERRORIST_STATE = '#RussiaIsATerroristState'
    RUSSIA_IS_A_TERRORIST_STATE_LO = '#russiaisaterrorisstate'
    STAND_WITH_UKRAINE = '#StandWithUkraine'
    STOP_RUSSIA = '#StopRussia'
    UKRAINE_RUSSIA_WAR = '#UkraineRussiaWar'
    PUTIN_WAR_CRIMINAL = '#PutinWarCriminal'
