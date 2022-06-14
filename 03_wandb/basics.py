from path import Path
import wandb

from imind.globals.ipaths import PCRelativeEnvConfig

# wandb.login()  # optional

def test_run(name, dir):
    
    #  `wandb.init()` spawns a new background process to log data to a run, and it
    # also syncs data to wandb.ai by default so you can see live visualizations.
    wandb.init(project="test-project2", entity="imindlabs", name=name, dir=dir)

    # `wandb.init()` returns a run object, and you can also access the run object
    # via `wandb.run`:
    # run = wandb.init()
    # assert run is wandb.run
        
        
    # wandb.config is a Config object which can be updated like a dictionary.
    # It will be set during init to an empty Config object if not provided
    wandb.config.update({
        "learning_rate": 0.001,
        "epochs": 100,
        "batch_size": 128
    })
       
    wandb.log({"loss": 50})
    wandb.log({"loss": 100})
    wandb.log({"loss": 110})
    wandb.log({"loss": 115})
    wandb.log({"loss": 150})
    wandb.log({"loss": 200})
    print("CONFIG:", wandb.config)
    
    wandb.config.update({
        "learning_rate": 0.001,
        "epochs": 200,
        "batch_size": 128
    }, allow_val_change=True)
        
    # # Sending an alert (will be notified via email or slack)
    # acc = 56
    # thresh = 80
    # wandb.alert(
    #     title="Low accuracy", 
    #     text=f"Accuracy {acc} is below the acceptable threshold {thresh}"
    # )
    # # title: (str) The title of the alert, must be less than 64 characters long.
    # # text: (str) The text body of the alert.
    # # level: (str or wandb.AlertLevel, optional) The alert level to use, either: `INFO`, `WARN`, or `ERROR`.
    # # wait_duration: (int, float, or timedelta, optional) The time to wait (in seconds) before sending another
    # #                   alert with this title.


    # At the end of your script, we will automatically call `wandb.finish` to
    # finalize and cleanup the run. However, if you call `wandb.init` from a
    # child process, you must explicitly call `wandb.finish` at the end of the
    # child process.
    wandb.finish()
    
test_run("test-run-103", Path(PCRelativeEnvConfig.get_path("DLN_PATH"))/"tutorials"/"03_wandb")
