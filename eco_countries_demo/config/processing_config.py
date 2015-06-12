processing = [
    {
        "band": 1,
        "process": [
            {
                "extract_bands": ""
            }
        ]
    },
    {
        "band": 1,
        "output_file_name": "merge",
        "process": [
            {
                "gdal_merge": {
                    "prefix": "gdal_merge_",
                    "extension": "tif"
                }
            }
        ]
    },
    {
        "band": 1,
        "output_file_name": "final",
        "process": [
            {
                "get_pixel_size" : "{{PIXEL_SIZE}}"
            },
            {
                "gdalwarp": {
                    "opt": {
                        "-multi": "",
                        "-overwrite": "",
                        "-of": "GTiff",
                        "-s_srs": "'+proj=sinu +R=6371007.181 +nadgrids=@null +wktext'",
                        "-co": "'TILED=YES'",
                        "-t_srs": "EPSG:3857",
                        "-srcnodata": -3000,
                        "-dstnodata": -3000
                    },
                    "prefix": "gdalwarp_",
                    "extension": "tif"
                }
            }
        ]
    },
    {
        "band": 1,
        "process": [
            {
                "gdaladdo": {
                    "parameters": {
                        "-r": "average"
                    },
                    "overviews_levels": "2 4 8 16"
                }
            }
        ]
    }
]
