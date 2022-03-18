import flopy
import os

def main():
    model_ws = os.path.join('model_ws','freyberg.usg')

    mf = flopy.mfusg.MfUsg.load('freyberg.usg.nam',model_ws=model_ws,version='mfusg',check=False,
                                    forgive=True,verbose=False, load_only=['disu','lpf','wel','ghb','rch'])


    # convert to all open/close
    ext_model_ws = os.path.join('model_ws','freyberg.usg.ext')
    mf.external_path = "."
    if os.path.exists(ext_model_ws):
        shutil.rmtree(ext_model_ws)
    # change dir and write
    mf.change_model_ws(etx_model_ws, reset_external=True)
    mf.write_input()


if __name__ == '__main__':
    main()
