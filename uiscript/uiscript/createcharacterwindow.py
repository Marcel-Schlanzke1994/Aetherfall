import uiScriptLocale
import aetherfalllayout

AETHERFALL_SELECT_PATH = "d:/ymir work/ui/aetherfall/select/"
AETHERFALL_CHARACTER_PATH = "d:/ymir work/ui/aetherfall/character/"
AETHERFALL_LOGIN_PATH = "d:/ymir work/ui/aetherfall/login/"

LEFT_PANEL_X = aetherfalllayout.anchor_left(28)
LEFT_PANEL_Y = 76
LEFT_PANEL_W = 420

RIGHT_PANEL_W = 336
RIGHT_PANEL_X = aetherfalllayout.anchor_right(SCREEN_WIDTH, RIGHT_PANEL_W, 28)
RIGHT_PANEL_Y = LEFT_PANEL_Y

BOTTOM_ACTION_Y = aetherfalllayout.anchor_bottom(SCREEN_HEIGHT, 78, 12)
PANEL_H = max(468, min(560, SCREEN_HEIGHT - 292))

DESCRIPTION_X = LEFT_PANEL_X
DESCRIPTION_Y = LEFT_PANEL_Y + PANEL_H + 14
DESCRIPTION_W = LEFT_PANEL_W
DESCRIPTION_H = 102

NAME_PANEL_W = 320
NAME_PANEL_OUTER_W = NAME_PANEL_W + 52
NAME_PANEL_X = aetherfalllayout.center_x(SCREEN_WIDTH, NAME_PANEL_OUTER_W)
NAME_PANEL_Y = DESCRIPTION_Y + 4

window = {
    "name": "CreateCharacterWindow",
    "x": 0,
    "y": 0,
    "width": SCREEN_WIDTH,
    "height": SCREEN_HEIGHT,
    "children": (
        {
            "name": "BackGround",
            "type": "expanded_image",
            "x": 0,
            "y": 0,
            "image": AETHERFALL_SELECT_PATH + "select_myr.sub",
            "x_scale": float(SCREEN_WIDTH) / 1024.0,
            "y_scale": float(SCREEN_HEIGHT) / 768.0,
        },
        {
            "name": "LeftPanel",
            "type": "window",
            "x": LEFT_PANEL_X,
            "y": LEFT_PANEL_Y,
            "width": LEFT_PANEL_W,
            "height": PANEL_H,
            "children": (
                {"name": "LeftPanelShade", "type": "bar", "x": 0, "y": 0, "width": LEFT_PANEL_W, "height": PANEL_H, "color": 0xb0090b10},
                {"name": "LeftPanelGlow", "type": "bar", "x": 1, "y": 1, "width": LEFT_PANEL_W - 2, "height": PANEL_H - 2, "color": 0x66322319},
                {"name": "FactionHeader", "type": "text", "x": 22, "y": 20, "text": "1. Fraktion waehlen"},
                {"name": "faction_button_a", "type": "button", "x": 22, "y": 52, "default_image": AETHERFALL_CHARACTER_PATH + "faction_mora_card.sub", "over_image": AETHERFALL_CHARACTER_PATH + "faction_mora_card.sub", "down_image": AETHERFALL_CHARACTER_PATH + "faction_mora_card.sub"},
                {"name": "faction_button_b", "type": "button", "x": 152, "y": 52, "default_image": AETHERFALL_CHARACTER_PATH + "faction_myr_purple_card.sub", "over_image": AETHERFALL_CHARACTER_PATH + "faction_myr_purple_card.sub", "down_image": AETHERFALL_CHARACTER_PATH + "faction_myr_purple_card.sub"},
                {"name": "faction_button_c", "type": "button", "x": 282, "y": 52, "default_image": AETHERFALL_CHARACTER_PATH + "faction_myr_blue_card.sub", "over_image": AETHERFALL_CHARACTER_PATH + "faction_myr_blue_card.sub", "down_image": AETHERFALL_CHARACTER_PATH + "faction_myr_blue_card.sub"},
                {"name": "ClassHeader", "type": "text", "x": 22, "y": 154, "text": "2. Klasse waehlen"},
                {"name": "slot_frame_0", "type": "bar", "x": 22, "y": 188, "width": 178, "height": 54, "color": 0x55201711},
                {"name": "slot_frame_1", "type": "bar", "x": 220, "y": 188, "width": 178, "height": 54, "color": 0x55201711},
                {"name": "slot_frame_2", "type": "bar", "x": 22, "y": 256, "width": 178, "height": 54, "color": 0x55201711},
                {"name": "slot_frame_3", "type": "bar", "x": 220, "y": 256, "width": 178, "height": 54, "color": 0x55201711},
                {"name": "slot_frame_4", "type": "bar", "x": 22, "y": 324, "width": 178, "height": 54, "color": 0x55201711},
                {"name": "slot_frame_5", "type": "bar", "x": 220, "y": 324, "width": 178, "height": 54, "color": 0x55201711},
                {"name": "slot_button_0", "type": "button", "x": 22, "y": 188, "default_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "over_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "down_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub"},
                {"name": "slot_button_1", "type": "button", "x": 220, "y": 188, "default_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "over_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "down_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub"},
                {"name": "slot_button_2", "type": "button", "x": 22, "y": 256, "default_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "over_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "down_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub"},
                {"name": "slot_button_3", "type": "button", "x": 220, "y": 256, "default_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "over_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "down_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub"},
                {"name": "slot_button_4", "type": "button", "x": 22, "y": 324, "default_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "over_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "down_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub"},
                {"name": "slot_button_5", "type": "button", "x": 220, "y": 324, "default_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "over_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "down_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub"},
                {"name": "name_warrior", "type": "image", "x": 34, "y": 202, "image": AETHERFALL_CHARACTER_PATH + "class_klingenwaechter.sub"},
                {"name": "name_assassin", "type": "image", "x": 232, "y": 202, "image": AETHERFALL_CHARACTER_PATH + "class_schattenlaeufer.sub"},
                {"name": "name_sura", "type": "image", "x": 34, "y": 270, "image": AETHERFALL_CHARACTER_PATH + "class_runenmagier.sub"},
                {"name": "name_shaman", "type": "image", "x": 232, "y": 270, "image": AETHERFALL_CHARACTER_PATH + "class_seelenrufer.sub"},
                {"name": "name_eisenjaeger", "type": "image", "x": 34, "y": 338, "image": AETHERFALL_CHARACTER_PATH + "class_eisenjaeger.sub"},
                {"name": "name_aetherbrut", "type": "image", "x": 232, "y": 338, "image": AETHERFALL_CHARACTER_PATH + "class_aetherbrut.sub"},
                {"name": "GenderHeader", "type": "text", "x": 22, "y": 394, "text": "3. Geschlecht"},
                {"name": "gender_button_01", "type": "radio_button", "x": 22, "y": 426, "default_image": AETHERFALL_CHARACTER_PATH + "gender_maennlich_selected.sub", "over_image": AETHERFALL_CHARACTER_PATH + "gender_maennlich_selected.sub", "down_image": AETHERFALL_CHARACTER_PATH + "gender_maennlich_selected.sub"},
                {"name": "gender_button_02", "type": "radio_button", "x": 170, "y": 426, "default_image": AETHERFALL_CHARACTER_PATH + "gender_weiblich.sub", "over_image": AETHERFALL_CHARACTER_PATH + "gender_weiblich.sub", "down_image": AETHERFALL_CHARACTER_PATH + "gender_weiblich.sub"},
                {"name": "left_button", "type": "button", "x": 250, "y": 418, "default_image": AETHERFALL_LOGIN_PATH + "btn_options_normal.sub", "over_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub", "down_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub", "text": "<"},
                {"name": "right_button", "type": "button", "x": 324, "y": 418, "default_image": AETHERFALL_LOGIN_PATH + "btn_options_normal.sub", "over_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub", "down_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub", "text": ">"},
            ),
        },
        {
            "name": "RightPanel",
            "type": "window",
            "x": RIGHT_PANEL_X,
            "y": RIGHT_PANEL_Y,
            "width": RIGHT_PANEL_W,
            "height": PANEL_H,
            "children": (
                {"name": "RightPanelShade", "type": "bar", "x": 0, "y": 0, "width": RIGHT_PANEL_W, "height": PANEL_H, "color": 0xb0090b10},
                {"name": "RightPanelGlow", "type": "bar", "x": 1, "y": 1, "width": RIGHT_PANEL_W - 2, "height": PANEL_H - 2, "color": 0x66322319},
                {"name": "CustomizationHeader", "type": "text", "x": 20, "y": 20, "text": "4. Aussehen anpassen"},
                {"name": "shape_button_01", "type": "radio_button", "x": 20, "y": 52, "default_image": AETHERFALL_CHARACTER_PATH + "tab_koerper_selected.sub", "over_image": AETHERFALL_CHARACTER_PATH + "tab_koerper_selected.sub", "down_image": AETHERFALL_CHARACTER_PATH + "tab_koerper_selected.sub"},
                {"name": "shape_button_02", "type": "radio_button", "x": 86, "y": 52, "default_image": AETHERFALL_CHARACTER_PATH + "tab_gesicht.sub", "over_image": AETHERFALL_CHARACTER_PATH + "tab_gesicht.sub", "down_image": AETHERFALL_CHARACTER_PATH + "tab_gesicht.sub"},
                {"name": "tab_haare_preview", "type": "image", "x": 152, "y": 52, "image": AETHERFALL_CHARACTER_PATH + "tab_haare.sub"},
                {"name": "tab_merkmale_preview", "type": "image", "x": 218, "y": 52, "image": AETHERFALL_CHARACTER_PATH + "tab_merkmale.sub"},
                {"name": "tab_details_preview", "type": "image", "x": 284, "y": 52, "image": AETHERFALL_CHARACTER_PATH + "tab_details.sub"},
                {"name": "BodyLabel", "type": "text", "x": 20, "y": 126, "text": "Koerperbau"},
                {"name": "BodyTrack", "type": "bar", "x": 20, "y": 152, "width": 296, "height": 8, "color": 0x55332219},
                {"name": "BodyKnob", "type": "bar", "x": 188, "y": 146, "width": 18, "height": 18, "color": 0xffc79547},
                {"name": "HeightLabel", "type": "text", "x": 20, "y": 190, "text": "Groesse"},
                {"name": "HeightTrack", "type": "bar", "x": 20, "y": 216, "width": 296, "height": 8, "color": 0x55332219},
                {"name": "HeightKnob", "type": "bar", "x": 214, "y": 210, "width": 18, "height": 18, "color": 0xffc79547},
                {"name": "HairColorLabel", "type": "text", "x": 20, "y": 252, "text": "Haarfarbe"},
                {"name": "HairColor0", "type": "bar", "x": 20, "y": 280, "width": 28, "height": 28, "color": 0xffe6e2d0},
                {"name": "HairColor1", "type": "bar", "x": 58, "y": 280, "width": 28, "height": 28, "color": 0xffad834a},
                {"name": "HairColor2", "type": "bar", "x": 96, "y": 280, "width": 28, "height": 28, "color": 0xff6a4b36},
                {"name": "HairColor3", "type": "bar", "x": 134, "y": 280, "width": 28, "height": 28, "color": 0xff221f20},
                {"name": "HairColor4", "type": "bar", "x": 172, "y": 280, "width": 28, "height": 28, "color": 0xff7f1d23},
                {"name": "HairColor5", "type": "bar", "x": 210, "y": 280, "width": 28, "height": 28, "color": 0xff64308c},
                {"name": "HairColor6", "type": "bar", "x": 248, "y": 280, "width": 28, "height": 28, "color": 0xff325999},
                {"name": "SkinLabel", "type": "text", "x": 20, "y": 330, "text": "Hautfarbe"},
                {"name": "Skin0", "type": "bar", "x": 20, "y": 358, "width": 34, "height": 22, "color": 0xffeed5c1},
                {"name": "Skin1", "type": "bar", "x": 62, "y": 358, "width": 34, "height": 22, "color": 0xffdfb89b},
                {"name": "Skin2", "type": "bar", "x": 104, "y": 358, "width": 34, "height": 22, "color": 0xffc99574},
                {"name": "Skin3", "type": "bar", "x": 146, "y": 358, "width": 34, "height": 22, "color": 0xffad7c5f},
                {"name": "Skin4", "type": "bar", "x": 188, "y": 358, "width": 34, "height": 22, "color": 0xff8d614a},
                {"name": "Skin5", "type": "bar", "x": 230, "y": 358, "width": 34, "height": 22, "color": 0xff6b4734},
                {"name": "Skin6", "type": "bar", "x": 272, "y": 358, "width": 34, "height": 22, "color": 0xff43281f},
                {"name": "EyeLabel", "type": "text", "x": 20, "y": 400, "text": "Augenfarbe"},
                {"name": "Eye0", "type": "bar", "x": 20, "y": 428, "width": 34, "height": 22, "color": 0xff1f5db8},
                {"name": "Eye1", "type": "bar", "x": 62, "y": 428, "width": 34, "height": 22, "color": 0xff3b7a26},
                {"name": "Eye2", "type": "bar", "x": 104, "y": 428, "width": 34, "height": 22, "color": 0xffaf8a32},
                {"name": "Eye3", "type": "bar", "x": 146, "y": 428, "width": 34, "height": 22, "color": 0xff2e99bb},
                {"name": "Eye4", "type": "bar", "x": 188, "y": 428, "width": 34, "height": 22, "color": 0xff6735a1},
                {"name": "Eye5", "type": "bar", "x": 230, "y": 428, "width": 34, "height": 22, "color": 0xff8f41c2},
                {"name": "Eye6", "type": "bar", "x": 272, "y": 428, "width": 34, "height": 22, "color": 0xff6d101d},
            ),
        },
        {
            "name": "text_board",
            "type": "window",
            "x": DESCRIPTION_X,
            "y": DESCRIPTION_Y,
            "width": DESCRIPTION_W,
            "height": DESCRIPTION_H,
            "children": (
                {"name": "text_board_back", "type": "bar", "x": 0, "y": 0, "width": DESCRIPTION_W, "height": DESCRIPTION_H, "color": 0xaa090b10},
                {"name": "text_board_glow", "type": "bar", "x": 1, "y": 1, "width": DESCRIPTION_W - 2, "height": DESCRIPTION_H - 2, "color": 0x66322319},
                {"name": "prev_button", "type": "button", "x": 0, "y": 44, "default_image": AETHERFALL_CHARACTER_PATH + "btn_zurueck.sub", "over_image": AETHERFALL_CHARACTER_PATH + "btn_zurueck.sub", "down_image": AETHERFALL_CHARACTER_PATH + "btn_zurueck.sub", "text": "<"},
                {"name": "next_button", "type": "button", "x": 183, "y": 44, "default_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "over_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "down_image": AETHERFALL_CHARACTER_PATH + "btn_name_pruefen.sub", "text": ">"},
            ),
        },
        {
            "name": "NamePanel",
            "type": "window",
            "x": NAME_PANEL_X,
            "y": NAME_PANEL_Y,
            "width": NAME_PANEL_OUTER_W,
            "height": 98,
            "children": (
                {"name": "NamePanelBack", "type": "bar", "x": 0, "y": 0, "width": NAME_PANEL_OUTER_W, "height": 98, "color": 0xaa090b10},
                {"name": "NamePanelGlow", "type": "bar", "x": 1, "y": 1, "width": NAME_PANEL_OUTER_W - 2, "height": 96, "color": 0x66322319},
                {"name": "NameHeader", "type": "text", "x": 0, "y": 14, "width": NAME_PANEL_OUTER_W, "height": 18, "horizontal_align": "center", "text_horizontal_align": "center", "text": "5. Charaktername"},
                {"name": "character_name_slot", "type": "image", "x": 26, "y": 40, "image": AETHERFALL_CHARACTER_PATH + "input_character_name.sub"},
                {"name": "character_name_value", "type": "editline", "x": 54, "y": 60, "width": 240, "height": 18, "input_limit": 12, "r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0},
            ),
        },
        {
            "name": "create_button",
            "type": "button",
            "x": SCREEN_WIDTH - 428,
            "y": BOTTOM_ACTION_Y,
            "default_image": AETHERFALL_CHARACTER_PATH + "btn_abenteuer_beginnen.sub",
            "over_image": AETHERFALL_CHARACTER_PATH + "btn_abenteuer_beginnen.sub",
            "down_image": AETHERFALL_CHARACTER_PATH + "btn_abenteuer_beginnen.sub",
            "text": uiScriptLocale.CREATE_CREATE,
        },
        {
            "name": "cancel_button",
            "type": "button",
            "x": 28,
            "y": BOTTOM_ACTION_Y,
            "default_image": AETHERFALL_CHARACTER_PATH + "btn_zurueck.sub",
            "over_image": AETHERFALL_CHARACTER_PATH + "btn_zurueck.sub",
            "down_image": AETHERFALL_CHARACTER_PATH + "btn_zurueck.sub",
            "text": uiScriptLocale.CANCEL,
        },
        {"name": "hth_gauge", "type": "gauge", "x": -200, "y": -200, "width": 1, "color": "red"},
        {"name": "int_gauge", "type": "gauge", "x": -200, "y": -200, "width": 1, "color": "yellow"},
        {"name": "str_gauge", "type": "gauge", "x": -200, "y": -200, "width": 1, "color": "purple"},
        {"name": "dex_gauge", "type": "gauge", "x": -200, "y": -200, "width": 1, "color": "blue"},
        {"name": "hth_value", "type": "text", "x": -200, "y": -200, "text": "0"},
        {"name": "int_value", "type": "text", "x": -200, "y": -200, "text": "0"},
        {"name": "str_value", "type": "text", "x": -200, "y": -200, "text": "0"},
        {"name": "dex_value", "type": "text", "x": -200, "y": -200, "text": "0"},
        {"name": "hth_button", "type": "button", "x": -220, "y": -220, "default_image": AETHERFALL_LOGIN_PATH + "btn_options_normal.sub", "over_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub", "down_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub"},
        {"name": "int_button", "type": "button", "x": -220, "y": -220, "default_image": AETHERFALL_LOGIN_PATH + "btn_options_normal.sub", "over_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub", "down_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub"},
        {"name": "str_button", "type": "button", "x": -220, "y": -220, "default_image": AETHERFALL_LOGIN_PATH + "btn_options_normal.sub", "over_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub", "down_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub"},
        {"name": "dex_button", "type": "button", "x": -220, "y": -220, "default_image": AETHERFALL_LOGIN_PATH + "btn_options_normal.sub", "over_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub", "down_image": AETHERFALL_LOGIN_PATH + "btn_options_hover.sub"},
    ),
}
