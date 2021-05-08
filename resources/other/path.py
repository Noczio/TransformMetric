normal_path: dict = {"Metrics": {"Path": ".\\resources\\info\\metrics.json"}}
debug_path: dict = {"Metrics": {"Path": ".\\..\\resources\\info\\metrics.json"}}

execution_metric_options: dict = {True: debug_path["Metrics"]["Path"],
                                  False: normal_path["Metrics"]["Path"]}
