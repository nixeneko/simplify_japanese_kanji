# coding: utf-8

unicode_version = "14.0.0"

import unicodedata

def load_conv_file(filename):
    ret_dict = {}
    with open(filename, "r") as f:
        for line in f:
            items = line.strip().split("\t")
            if len(items)>0:
                ret_dict[items[0]] = items[1]
    return ret_dict

conversion_dict = {}
conversion_dict.update(load_conv_file("single_conversion_candidate.txt"))
conversion_dict.update(load_conv_file("multiple_candidate_selected.txt"))

sin_preffered = {   "羽":"羽","益":"益","囘":"回","悔":"悔","海":"海","慨":"慨","槪":"概","喝":"喝",
                    "褐":"褐","器":"器","既":"既","旣":"既","祈":"祈","敎":"教","勤":"勤","羣":"群",
                    "契":"契","硏":"研","祉":"祉","煮":"煮","社":"社","者":"者","臭":"臭","祝":"祝",
                    "暑":"暑","署":"署","敍":"叙","尙":"尚","牀":"床","祥":"祥","愼":"慎","眞":"真",
                    "神":"神","刄":"刃","晴":"晴","淸":"清","精":"精","靑":"青","祖":"祖","僧":"僧",
                    "憎":"憎","卽":"即","琢":"琢","癡":"痴","猪":"猪","都":"都","突":"突","姙":"妊",
                    "梅":"梅","繁":"繁","卑":"卑","碑":"碑","祕":"秘","敏":"敏","甁":"瓶","侮":"侮",
                    "福":"福","勉":"勉","萠":"萌","襃":"褒","墨":"墨","飜":"翻","槇":"槙","免":"免",
                    "戾":"戻","祐":"祐","慾":"欲","畧":"略","隆":"隆","旅":"旅","廉":"廉","廊":"廊",
                    "朗":"朗","郞":"郎","亙":"亘"}
different_simp = {  "郷":"乡","鄕":"乡","勲":"勋","勳":"勋","鶏":"鸡","鷄":"鸡","渋":"涩","澁":"涩",
                    "浄":"净","淨":"净","塚":"冢","塚":"冢","闘":"斗","鬭":"斗","鬪":"斗",
                    "塀":"垣","塀":"垣","舗":"铺","舖":"铺"}
#not sure
#弁 辨 →辨(multiple)
#弁 瓣 →瓣(multiple)
#粘←黏 (どちらも使うっぽい)
#予 豫 (コンテキストによる)
def conv_different_simp(text):
    return text.translate(str.maketrans(different_simp))
#additional = {"敎":"教", "爲":"为", "嶽":"岳", "敎":"教", "飮":"饮", "衞":"卫", "謁":"谒",
#              "囘":"回", "槪":"概", "漢":"汉", "旣":"既", }
#conversion_dict.update(additional)

def trad2simp(text):
    global conversion_dict
    return text.translate(str.maketrans(conversion_dict))


sin = "亜悪圧囲為医壱逸稲飲隠羽営栄衛鋭益駅悦謁閲円縁艶塩奥応横欧殴黄温穏仮価禍画会回壊悔懐海絵慨概拡殻覚学岳楽喝渇褐鎌勧巻寛歓漢缶観関陥館顔器既既帰気祈亀偽戯犠却糾旧拠挙虚峡挟教強狭郷響尭暁勤謹区駆勲薫群契径恵掲携渓経継茎蛍軽鶏芸撃欠倹剣圏検権献県研険顕験厳戸呉娯効広恒鉱号国穀黒歳済砕斎剤冴桜冊殺雑産参惨桟蚕賛残祉姉糸視飼歯児辞湿実舎写煮社者釈寿収臭従渋獣縦祝粛処暑緒署諸叙尚奨将床渉焼祥称証乗剰壌嬢条浄状畳穣譲醸嘱触寝慎晋真神刃尽図粋酔随髄数枢瀬晴清精青声静斉税跡節説摂窃絶専戦浅潜繊践銭禅曽祖僧双壮層捜挿巣争痩窓総聡荘装騒増憎臓蔵贈即属続堕体対帯滞台滝択沢琢脱単嘆担胆団弾断痴遅着昼虫鋳猪著庁徴懲聴勅鎮塚逓鉄転点伝都党盗灯当闘闘徳独読突届縄難弐妊粘悩脳覇廃拝梅売麦発髪抜繁飯晩蛮卑碑秘彦姫浜賓頻敏瓶侮福払仏併塀並変辺勉弁弁弁舗歩穂宝萌褒豊墨没翻槙毎万満免麺黙餅戻弥薬訳祐予余与誉揺様謡遥瑶欲来頼乱欄覧略隆竜虜旅両猟緑隣凛塁涙類励礼隷霊齢暦歴廉恋練錬炉労廊朗楼郎禄録亘湾"
kyu = "亞惡壓圍爲醫壹逸稻飮隱羽營榮衞銳益驛悅謁閱圓緣艷鹽奧應橫歐毆黃溫穩假價禍畫會囘壞悔懷海繪慨槪擴殼覺學嶽樂喝渴褐鐮勸卷寬歡漢罐觀關陷館顏器既旣歸氣祈龜僞戲犧卻糺舊據擧虛峽挾敎强狹鄕響堯曉勤謹區驅勳薰羣契徑惠揭攜溪經繼莖螢輕鷄藝擊缺儉劍圈檢權獻縣硏險顯驗嚴戶吳娛效廣恆鑛號國穀黑歲濟碎齋劑冱櫻册殺雜產參慘棧蠶贊殘祉姊絲視飼齒兒辭濕實舍寫煮社者釋壽收臭從澁獸縱祝肅處暑緖署諸敍尙奬將牀涉燒祥稱證乘剩壤孃條淨狀疊穰讓釀囑觸寢愼晉眞神刄盡圖粹醉隨髓數樞瀨晴淸精靑聲靜齊稅蹟節說攝竊絕專戰淺潛纖踐錢禪曾祖僧雙壯層搜插巢爭瘦窗總聰莊裝騷增憎臟藏贈卽屬續墮體對帶滯臺瀧擇澤琢脫單嘆擔膽團彈斷癡遲著晝蟲鑄猪著廳徵懲聽敕鎭塚遞鐵轉點傳都黨盜燈當鬭鬪德獨讀突屆繩難貳姙黏惱腦霸廢拜梅賣麥發髮拔繁飯晚蠻卑碑祕彥姬濱賓頻敏甁侮福拂佛倂塀竝變邊勉辯辨瓣舖步穗寶萠襃豐墨沒飜槇每萬滿免麵默餠戾彌藥譯祐豫餘與譽搖樣謠遙瑤慾來賴亂欄覽畧隆龍虜旅兩獵綠鄰凜壘淚類勵禮隸靈齡曆歷廉戀練鍊爐勞廊朗樓郞祿錄亙灣"
sin2kyu_dict = {}
for s, k in zip(sin, kyu):
    if unicodedata.normalize("NFC", s) in conversion_dict:
        sin2kyu_dict[unicodedata.normalize("NFC", s)] = s
        sin2kyu_dict[unicodedata.normalize("NFC", k)] = s
    else:
        sin2kyu_dict[unicodedata.normalize("NFC", k)] = k
        sin2kyu_dict[unicodedata.normalize("NFC", s)] = k
        #print(s, k)
    #else:
        #print(s, k)

def sin2kyu(text):
    return unicodedata.normalize("NFC", text).translate(str.maketrans(sin2kyu_dict)).translate(str.maketrans(sin_preffered))
    
def jp2zh(text):
    return trad2simp(sin2kyu(text))



if __name__ == "__main__":
    t = """準備完了ですか？"""
    print(jp2zh(t))
    
    
    sin2zh_dict = dict(zip(sin, conv_different_simp(trad2simp(unicodedata.normalize("NFC", sin2kyu(sin))))))
    kyu2zh_dict = dict(zip(kyu, conv_different_simp(trad2simp(unicodedata.normalize("NFC", sin2kyu(sin))))))
    conversion_dict.update(sin2zh_dict)
    conversion_dict.update(kyu2zh_dict)
    js_unicodever = 'unicode_version="{}";\n'.format(unicode_version)
    js_dict ="jp2zh_dict={"
    for key in conversion_dict:
        if key != conversion_dict[key]:
            js_dict+= '"{}":"{}",'.format(key, conversion_dict[key])
    js_dict = js_dict[:-1]+"};\n" # Remove final comma
    with open("jp2zh.js", "w") as w:
        w.write(js_unicodever)
        w.write(js_dict)
