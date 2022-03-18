import flopy
import os

def main():
    model_ws = os.path.join('model_ws','freyberg.usg')

    mf = flopy.modflow.Modflow.load('freyberg.usg.nam',model_ws=model_ws,version='mfusg',check=True,
                                    load_only=['disu','bas6'],forgive=False,verbose=True)

if __name__ == '__main__':
    main()
    