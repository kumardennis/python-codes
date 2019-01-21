# 	Each respondent evaluates 6 different assets (brand stimuli) – so will get 6 implicit ‘tasks’
#	These assets need to be assigned completely randomized across respondents, however;
#	SELECTION RESTRICTION: maximum 2 assets of the same brand per respondent:

#   In this study we have 89 assets across 13 different brands:


import os
import random
# files = os.listdir("S:/1901/IBA66351")
#
# url = []
#
# for i in range(len(files)):
#     # img = "url('https://media.norstat.no/1901/IBA66351/" + str(files[i]) + "')"
#     img = str(files[i])
#     url.append(img);
#
# print(url)


urls = ['1001_Jacobs_logo.jpg', '1002_Jacobs_PackageElement_Coppaskinke.jpg', '1003_Jacobs_PackageElement_Italia.jpg', '1004_Jacobs_Packdesign.jpg', '101_Grilstad_currentlogo.jpg', '102_Grilstad_Oldlogo.jpg', '103_Grilstad_Jubel_subbrand.jpg', '104_Grilstad_CompanySlogan.jpg', '105_Grilstad_StructuralPackDesign_Bordpakning.jpg', '106_Grilstad_HistoricalPackage.jpg', '107_Grilstad_Jubel_subbrand.jpg', '108_Grilstad_Packaging_LevLittLettere.jpg', '109_Grilstad_Pepperoni_wholesausage.jpg', '1101_Folkets_logo.jpg', '1102_Folkets_text_GodHverdag.jpg', '1103_Folkets_packdesign.jpg', '110_Grilstad_ManFromAdvertisement.jpg', '111_Grilstad_Fenkel_PackSpecial.jpg', '112_Grilstad_Heigl_Subbrand.jpg', '113_Grilstad_GankseEnkeltKvalitet.jpg', '114_Grilstad_Text_ForGodtTilAVaereSunt.jpg', '115_Grilstad_Text_LevLittLettere.jpg', '116_Grilstad_Logo_LevLittLettere.jpg', '117_Grilstad_Advertisement_Houses.jpg', '118_Grilstad_SnackSausage.jpg', '119_Grilstad_1957.jpg', '120_Grilstad_ItalianSubbrand.jpg', '121_Grilstad_FrozenBurger.jpg', '122_Grilstad_JubelPack.jpg', '123_Grilstad_Jubel_J-device.jpg', '124_Grilstad_GullPack.jpg', '125_Grilstad_colours_BlackGold.jpg', '126_Grilstad_Text_Subbrand_Tronderfar.jpg', '127_Grilstad_Text_Subbrand_Jubelsalami.jpg', '128_Grilstad_Text_Subbrand_Gullsalami.jpg', '129_Grilstad_OldPepperoniPack.jpg', '130_Grilstad_PackPizzaPepperoni.jpg', '201_Gilde_Logo_RedWhite.jpg', '202_Gilde_Logo_RedBlue.jpg', '203_Gilde_colours_RedBlue.jpg', '204_Gilde_Text_Favorittsalami.jpg', '205_Gilde_Text_FraDenNorskeBonden.jpg', '206_Gilde_logo_Tynset.jpg', '207_Gilde_packdesign.jpg', '208_Gilde_packdesign_Pepperoni.jpg', '209_Gilde_text_Fjellskinke.jpg', '210_Gilde_text_Go&Mager.jpg', '211_Gilde_Packdesign_sausage.jpg', '212_Gilde_Packdesign_salami.jpg', '301_Vossafar_colours.jpg', '302_Vossafar_packdesign.jpg', '303_Vossafar_Woman.jpg', '304_Vossafar_Advertising.jpg', '401_Stranda_logo_blue.jpg', '402_Stranda_logo_BW.jpg', '403_Stranda_colour.jpg', '404_Stranda_pack_colour.jpg', '405_Stranda_pack_black.jpg', '406_Stranda_pack2_colour.jpg', '407_Stranda_pack3_Black.jpg', '408_Stranda_pack4_colour.jpg', '409_Stranda_pack5_Fjellbris_colour.jpg', '410_Stranda_Text_Commercial.jpg', '411_Stranda_Image_Commercial.jpg', '412_Stranda_Text_KanBareLagesPa.jpg', '413_Stranda_Text_Fjellbris.jpg', '414_Stranda_Text_Westfaler.jpg', '415_Stranda_image_MedEnVri.jpg', '501_Tind_logo.jpg', '502_Tind_package_old.jpg', '503_Tind_#02.jpg', '504_Tind_Package_new.jpg', '505_Tind_colours.jpg', '506_Tind_advertisment.jpg', '601_Tulip_logo.jpg', '602_Tulip_packageSalami.jpg', '603_Tulip_packageDanskSalami.jpg', '701_Coop_packdesign_Spekeskinke.jpg', '702_Coop_packdesign_Serranoskinke.jpg', '703_Coop_text_SmakForskjellenjpg.jpg', '801_Taga_logo.jpg', '802_Taga_designelement.jpg', '803_Taga_packdesign_redblack.jpg', '804_Taga_packdesign_Blackgrey.jpg', '805_Taga_colours.jpg', '901_Nordfjord_logo.jpg', '902_Nordfjord_Packdesign_DanskSalami.jpg', '903_Nordfjord_Packdesign_Salami.jpg', '904_Nordfjord_text_Stynskinke.jpg']




toShowArr = []



def func():
    randomUrl = random.sample(urls, len(urls))

    randome = random.sample(range(88), 6)
    print(randome)
    del toShowArr[:]
    for i in range(len(randome)):
        toShow = str(randomUrl[randome[i]])
        toShowArr.append(toShow)
        toShowArr.sort()

func()


brands = [
    "Jacobs",
    "Folkets",
    "Grilstad",
    "Gilde",
"Vossafar",
"Stranda",
"Tind",
"Tulip",
"Coop",
"Taga",
"Nordfjord",



]



for j in range(len(brands)):
    problem = True
    while problem == True:
        matching = [x for x in toShowArr if brands[j] in x]
        if len(matching) > 2:
            print(toShowArr)
            func()
            print("reroll")
            continue
        else:
            break
        problem = False


print(toShowArr)
print(len(toShowArr))




index = []
for i in range(len(toShowArr)):
    ind = urls.index(toShowArr[i])+1
    inds = "r"+str(ind)
    index.append(inds)

print(index)

    #
    # for j in range(89):
    #     if str(tasksHelp.attr('r%r' % (j+1)).label) == str(index[i]):
    #         tasksHelp.attr('r%r' % (j+1)).val = 1
    #
