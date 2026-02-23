def confidence_score(results):
    if not results:
        return "Low", 0.0

    avg_distance = sum(score for _, score in results) / len(results)


    if avg_distance >= 0.8:
        return "High", avg_distance
    elif avg_distance >= 0.65:
        return "Medium", avg_distance
    else:
        return "Low", avg_distance
