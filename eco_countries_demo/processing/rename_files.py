import os
import glob
from geobricks_common.core.filesystem import get_filename



def rename(path, from_basename, to_basename):
    files = glob.glob(path + "/*.tif")

    for f in files:
        if os.path.isfile(f):
            new_filename = get_filename(f).replace(from_basename, to_basename) + ".tif"
            os.rename(f, path + "/" + new_filename)


# path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/MYD11C3_ZSCORE/"
# rename(path, "LST_ZScore_6km_MYD11C3_200304", "LST_ZScore_6km_MYD11C3")

#path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/MYD11C3_ZSCORE/"
#rename(path, "6km_ZScore", "ZScore_6km")
#
#path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_ANOMALY/"
#rename(path, "6km_Anomaly", "Anomaly_6km")

# path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_ANOMALY/"
# rename(path, "MOD16A2", "MOD16A2_")
#
#path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_SD/"
#rename(path, "MOD16A2", "SD#_MOD16A2")
#
# path = "/media/vortex/LaCie/NENA_REGION/NENA_MOD13A3/NENA_MOD13A3_ANOMALY/"
# rename(path, "MOD13A3", "NDVI_Anomaly_1km_MOD13A3")

#
# # rename folders
# path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3"
# os.rename(path + "/avg", path + "/MYD11C3_AVG")
# os.rename(path + "/anomalies", path + "/MYD11C3_ANOMALY")
# os.rename(path + "/sd", path + "/MYD11C3_SD")
# os.rename(path + "/zscore", path + "/MYD11C3_ZSCORE")
# os.rename(path + "/variance", path + "/MYD11C3_VARIANCE")



