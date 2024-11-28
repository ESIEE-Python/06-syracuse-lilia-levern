#### Fonctions secondaires
"""jjjjj"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###

def syr_plot(lsyr):
    """ jjjjjjj"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    l = [n ]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(liste):
    """ Args:
        n (int): la source de la suite

         Returns:
        list: la suite de Syracuse de source n 
    """
# votre code ici
    if len(liste) == 0:
        idx = -999
    for idx, elt in enumerate(liste, 1):
        if elt==1:
            break
            # return idx

    return idx

def temps_de_vol_en_altitude(l):
    """jjj"""



  # votre code ici
    if len(l):
        return_value = -999
    altitude_initiale = l[0]
    for elt in l:
        if elt<altitude_initiale :
            return_value = l.index(elt)
            break

    return  return_value




def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # votre code ici
    n = max(l)
    return n


#### Fonction principale


def main():
    """jjjjj"""

    # vos appels à la fonction secondaire ici
    print((syracuse_l(5)))
    syr_plot(syracuse_l(5))
    print(temps_de_vol(syracuse_l(5)))
    print(temps_de_vol_en_altitude(syracuse_l(5)))
    print(altitude_maximale(syracuse_l(5)))
    lsyr = syracuse_l(15)

    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
