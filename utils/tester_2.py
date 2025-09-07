from utils.helpers import *
from config.paths_config import *
from pipeline.prediction_pipeline import hybrid_recommendation


#print(find_similar_animes("Fairy Tail", ANIME_WEIGHTS_PATH, ANIME2ANIME_ENCODED,ANIME2ANIME_DECODED, path_anime_df, n=10, return_dist=False, neg=False))

# similar_users = find_similar_users(11880,USER_WEIGHTS_PATH,USER2USER_ENCODED, USER2USER_DECODED,n=10, return_dist=False, neg=False)

#pref = get_user_preferences(11880, RATING_DF, DF)


print(hybrid_recommendation(11880))