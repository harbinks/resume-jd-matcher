from src.scoring.skill_tiers import SKILL_TIERS


def map_skills_to_tiers(skills: set) -> dict:
    """
    Map a set of skills to global tiers.
    Returns dict with keys: core, plus, bonus
    """
    tiered = {
        "core": set(),
        "plus": set(),
        "bonus": set()
    }

    for skill in skills:
        if skill in SKILL_TIERS["core"]:
            tiered["core"].add(skill)
        elif skill in SKILL_TIERS["plus"]:
            tiered["plus"].add(skill)
        elif skill in SKILL_TIERS["bonus"]:
            tiered["bonus"].add(skill)

    return tiered

if __name__ == "__main__":
    sample_skills = {
        "Java", "REST APIs", "SQL",
        "Cloud", "Kafka", "Docker"
    }

    print(map_skills_to_tiers(sample_skills))
