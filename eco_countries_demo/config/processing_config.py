processing = {
    "myd11c3": [
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
            "output_file_name": "semi.tif",
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
                            "-t_srs": "EPSG:3857"
                        },
                        "prefix": "gdalwarp_",
                        "extension": "tif"
                    }
                }
            ]
        },
        {
            "band": 1,
            "output_file_name": "final.tif",
            "process": [
                {
                    "gdal_translate": {
                        "opt": {
                            "-a_nodata": "-3000",
                            "-co": "'TILED=YES'",
                            "-co": "'COMPRESS=DEFLATE'"
                        }
                    }
                }
            ]
        }
    ],
    "mod13a3": [
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
            "output_file_name": "merge.tif",
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
            "output_file_name": "warp.tif",
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
                            "-t_srs": "EPSG:3857"
                        },
                        "prefix": "gdalwarp_",
                        "extension": "tif"
                    }
                }
            ]
        },
        {
            "band": 1,
            "output_file_name": "final.tif",
            "process": [
                {
                    "gdal_translate": {
                        "opt": {
                            "-a_nodata": "-3000",
                            "-co": "'TILED=YES'",
                            "-co": "'COMPRESS=DEFLATE'"
                        }
                    }
                }
            ]
        }
    ],
    "mod13a1": [
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
            "output_file_name": "merge.tif",
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
            "output_file_name": "warp.tif",
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
                            "-t_srs": "EPSG:3857"
                        },
                        "prefix": "gdalwarp_",
                        "extension": "tif"
                    }
                }
            ]
        },
        {
            "band": 1,
            "output_file_name": "final.tif",
            "process": [
                {
                    "gdal_translate": {
                        "opt": {
                            "-a_nodata": "-3000",
                            "-co": "'TILED=YES'",
                            "-co": "'COMPRESS=DEFLATE'"
                        }
                    }
                }
            ]
        }
    ],
    "mod16": [
        {
            "band": 1,
            "output_file_name": "warp.tif",
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
                            "-s_srs": "EPSG:4326",
                            "-t_srs": "EPSG:3857"
                        },
                        "prefix": "gdalwarp_",
                        "extension": "tif"
                    }
                }
            ]
        },
        {
            "band": 1,
            "output_file_name": "final.tif",
            "process": [
                {
                    "gdal_translate": {
                        "opt": {
                            "-a_nodata": "-3000",
                            "-co": "'TILED=YES'",
                            "-co": "'COMPRESS=DEFLATE'"
                        }
                    }
                }
            ]
        }
    ]
}