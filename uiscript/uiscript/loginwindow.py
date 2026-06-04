import uiScriptLocale
import aetherfalllayout

AETHERFALL_LOGIN_PATH = "d:/ymir work/ui/aetherfall/login/"

LOGIN_BG = AETHERFALL_LOGIN_PATH + "login_bg_1024x768.sub"
LOGO_IMAGE = AETHERFALL_LOGIN_PATH + "aetherfall_logo.sub"
LOGIN_FIELD = AETHERFALL_LOGIN_PATH + "input_normal.sub"
LOGIN_BUTTON = AETHERFALL_LOGIN_PATH + "btn_login_normal.sub"
LOGIN_BUTTON_OVER = AETHERFALL_LOGIN_PATH + "btn_login_hover.sub"
LOGIN_BUTTON_DOWN = AETHERFALL_LOGIN_PATH + "btn_login_down.sub"
REGISTER_BUTTON = AETHERFALL_LOGIN_PATH + "btn_register_normal.sub"
REGISTER_BUTTON_OVER = AETHERFALL_LOGIN_PATH + "btn_register_hover.sub"
OPTIONS_BUTTON = AETHERFALL_LOGIN_PATH + "btn_options_normal.sub"
OPTIONS_BUTTON_OVER = AETHERFALL_LOGIN_PATH + "btn_options_hover.sub"
SERVER_FRAME = AETHERFALL_LOGIN_PATH + "server_select_normal.sub"
SERVER_FRAME_OVER = AETHERFALL_LOGIN_PATH + "server_select_hover.sub"
SERVER_DOT = AETHERFALL_LOGIN_PATH + "server_online_dot.sub"
SERVER_ARROW = AETHERFALL_LOGIN_PATH + "server_dropdown_arrow.sub"

ID_LIMIT_COUNT = 19
PW_LIMIT_COUNT = 16

PANEL_WIDTH = 430
SELECT_BUTTON_WIDTH = 402
LOGIN_PANEL_HEIGHT = 392
SERVER_PANEL_WIDTH = max(700, min(860, SCREEN_WIDTH - 84))
SERVER_PANEL_HEIGHT = 322
UTILITY_BUTTON_WIDTH = 94
UTILITY_BUTTON_GAP = 14
UTILITY_BAR_WIDTH = (UTILITY_BUTTON_WIDTH * 3) + (UTILITY_BUTTON_GAP * 2)

LOGIN_X = aetherfalllayout.center_x(SCREEN_WIDTH, PANEL_WIDTH)
CONNECT_Y = max(278, aetherfalllayout.center_y(SCREEN_HEIGHT, 420))
LOGIN_Y = CONNECT_Y + 92
SERVER_X = aetherfalllayout.center_x(SCREEN_WIDTH, SERVER_PANEL_WIDTH)
SERVER_Y = max(136, aetherfalllayout.center_y(SCREEN_HEIGHT, SERVER_PANEL_HEIGHT))
UTILITY_Y = aetherfalllayout.anchor_bottom(SCREEN_HEIGHT, 97, 18)
LIST_WIDTH = 384
CHANNEL_WIDTH = 190

window = {
    "name": "LoginWindow",
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
            "image": LOGIN_BG,
            "x_scale": float(SCREEN_WIDTH) / 1024.0,
            "y_scale": float(SCREEN_HEIGHT) / 768.0,
        },
        {
            "name": "AetherfallLogo",
            "type": "expanded_image",
            "x": aetherfalllayout.center_x(SCREEN_WIDTH, 575),
            "y": 24,
            "image": LOGO_IMAGE,
            "x_scale": 0.30,
            "y_scale": 0.30,
        },
        {
            "name": "ConnectBoard",
            "type": "window",
            "x": LOGIN_X,
            "y": CONNECT_Y,
            "width": PANEL_WIDTH,
            "height": 86,
            "children": (
                {"name": "ConnectBoardShade", "type": "bar", "x": 0, "y": 0, "width": PANEL_WIDTH, "height": 86, "color": 0xb0090b10},
                {"name": "ConnectBoardGlow", "type": "bar", "x": 1, "y": 1, "width": PANEL_WIDTH - 2, "height": 84, "color": 0x66322319},
                {
                    "name": "SelectConnectButton",
                    "type": "button",
                    "x": 14,
                    "y": 8,
                    "default_image": SERVER_FRAME,
                    "over_image": SERVER_FRAME_OVER,
                    "down_image": SERVER_FRAME_OVER,
                    "text": "",
                },
                {"name": "ConnectOnlineDot", "type": "image", "x": 34, "y": 31, "image": SERVER_DOT},
                {
                    "name": "ConnectName",
                    "type": "text",
                    "x": 60,
                    "y": 0,
                    "width": 280,
                    "height": 72,
                    "vertical_align": "center",
                    "text_vertical_align": "center",
                    "text": uiScriptLocale.LOGIN_DEFAULT_SERVERADDR,
                },
                {"name": "ConnectArrow", "type": "image", "x": 360, "y": 28, "image": SERVER_ARROW},
            ),
        },
        {
            "name": "LoginBoard",
            "type": "window",
            "x": LOGIN_X,
            "y": LOGIN_Y,
            "width": PANEL_WIDTH,
            "height": LOGIN_PANEL_HEIGHT,
            "children": (
                {"name": "LoginPanelShade", "type": "bar", "x": 0, "y": 0, "width": PANEL_WIDTH, "height": LOGIN_PANEL_HEIGHT, "color": 0xb0090b10},
                {"name": "LoginPanelGlow", "type": "bar", "x": 1, "y": 1, "width": PANEL_WIDTH - 2, "height": LOGIN_PANEL_HEIGHT - 2, "color": 0x66322319},
                {"name": "ID_Field", "type": "image", "x": 16, "y": 26, "image": LOGIN_FIELD},
                {"name": "Password_Field", "type": "image", "x": 16, "y": 102, "image": LOGIN_FIELD},
                {"name": "ID_Icon", "type": "image", "x": 34, "y": 45, "image": AETHERFALL_LOGIN_PATH + "icon_user.sub"},
                {"name": "Password_Icon", "type": "image", "x": 34, "y": 121, "image": AETHERFALL_LOGIN_PATH + "icon_lock.sub"},
                {"name": "ID_Text", "type": "text", "x": 68, "y": 32, "text": uiScriptLocale.LOGIN_ID},
                {"name": "Password_Text", "type": "text", "x": 68, "y": 108, "text": uiScriptLocale.LOGIN_PASSWORD},
                {
                    "name": "ID_EditLine",
                    "type": "editline",
                    "x": 68,
                    "y": 56,
                    "width": 300,
                    "height": 18,
                    "input_limit": ID_LIMIT_COUNT,
                    "r": 1.0,
                    "g": 1.0,
                    "b": 1.0,
                    "a": 1.0,
                },
                {
                    "name": "Password_EditLine",
                    "type": "editline",
                    "x": 68,
                    "y": 132,
                    "width": 300,
                    "height": 18,
                    "input_limit": PW_LIMIT_COUNT,
                    "secret_flag": 1,
                    "r": 1.0,
                    "g": 1.0,
                    "b": 1.0,
                    "a": 1.0,
                },
                {
                    "name": "LoginButton",
                    "type": "button",
                    "x": 12,
                    "y": 182,
                    "default_image": LOGIN_BUTTON,
                    "over_image": LOGIN_BUTTON_OVER,
                    "down_image": LOGIN_BUTTON_DOWN,
                    "text": uiScriptLocale.LOGIN_CONNECT,
                },
                {"name": "ErrorMessageArea", "type": "text", "x": 24, "y": 244, "width": 382, "height": 18, "text": ""},
                {
                    "name": "RegisterButton",
                    "type": "button",
                    "x": 54,
                    "y": 266,
                    "default_image": REGISTER_BUTTON,
                    "over_image": REGISTER_BUTTON_OVER,
                    "down_image": REGISTER_BUTTON_OVER,
                    "text": "Konto erstellen",
                },
                {
                    "name": "LoginExitButton",
                    "type": "button",
                    "x": 168,
                    "y": 296,
                    "default_image": OPTIONS_BUTTON,
                    "over_image": OPTIONS_BUTTON_OVER,
                    "down_image": OPTIONS_BUTTON_OVER,
                    "text": uiScriptLocale.LOGIN_EXIT,
                },
            ),
        },
        {
            "name": "ServerBoard",
            "type": "window",
            "x": SERVER_X,
            "y": SERVER_Y,
            "width": SERVER_PANEL_WIDTH,
            "height": SERVER_PANEL_HEIGHT,
            "children": (
                {"name": "ServerBoardBack", "type": "bar", "x": 0, "y": 0, "width": SERVER_PANEL_WIDTH, "height": SERVER_PANEL_HEIGHT, "color": 0xb0090b10},
                {"name": "ServerBoardGlow", "type": "bar", "x": 1, "y": 1, "width": SERVER_PANEL_WIDTH - 2, "height": SERVER_PANEL_HEIGHT - 2, "color": 0x66322319},
                {
                    "name": "Title",
                    "type": "text",
                    "x": 0,
                    "y": 20,
                    "width": SERVER_PANEL_WIDTH,
                    "height": 18,
                    "horizontal_align": "center",
                    "text_horizontal_align": "center",
                    "text": uiScriptLocale.LOGIN_SELECT_TITLE,
                },
                {"name": "ServerListBack", "type": "bar", "x": 24, "y": 62, "width": LIST_WIDTH, "height": 168, "color": 0x33201711},
                {"name": "ChannelListBack", "type": "bar", "x": SERVER_PANEL_WIDTH - CHANNEL_WIDTH - 24, "y": 62, "width": CHANNEL_WIDTH, "height": 168, "color": 0x33201711},
                {"name": "ServerList", "type": "listbox2", "x": 30, "y": 68, "width": LIST_WIDTH - 12, "height": 156, "row_count": 8, "item_align": 0},
                {"name": "ChannelList", "type": "listbox", "x": SERVER_PANEL_WIDTH - CHANNEL_WIDTH - 18, "y": 68, "width": CHANNEL_WIDTH - 12, "height": 156, "item_align": 0},
                {
                    "name": "ServerSelectButton",
                    "type": "button",
                    "x": 62,
                    "y": 242,
                    "default_image": LOGIN_BUTTON,
                    "over_image": LOGIN_BUTTON_OVER,
                    "down_image": LOGIN_BUTTON_DOWN,
                    "text": uiScriptLocale.OK,
                },
                {
                    "name": "ServerExitButton",
                    "type": "button",
                    "x": SERVER_PANEL_WIDTH - 384,
                    "y": 242,
                    "default_image": REGISTER_BUTTON,
                    "over_image": REGISTER_BUTTON_OVER,
                    "down_image": REGISTER_BUTTON_OVER,
                    "text": uiScriptLocale.LOGIN_SELECT_EXIT,
                },
            ),
        },
        {
            "name": "UtilityBar",
            "type": "window",
            "x": aetherfalllayout.center_x(SCREEN_WIDTH, UTILITY_BAR_WIDTH),
            "y": UTILITY_Y,
            "width": UTILITY_BAR_WIDTH,
            "height": 97,
            "children": (
                {"name": "AccountButton", "type": "button", "x": 0, "y": 0, "default_image": OPTIONS_BUTTON, "over_image": OPTIONS_BUTTON_OVER, "down_image": OPTIONS_BUTTON_OVER, "text": "Konto"},
                {"name": "LanguageButton", "type": "button", "x": UTILITY_BUTTON_WIDTH + UTILITY_BUTTON_GAP, "y": 0, "default_image": OPTIONS_BUTTON, "over_image": OPTIONS_BUTTON_OVER, "down_image": OPTIONS_BUTTON_OVER, "text": "Sprache"},
                {"name": "OptionsButton", "type": "button", "x": (UTILITY_BUTTON_WIDTH + UTILITY_BUTTON_GAP) * 2, "y": 0, "default_image": OPTIONS_BUTTON, "over_image": OPTIONS_BUTTON_OVER, "down_image": OPTIONS_BUTTON_OVER, "text": "Optionen"},
            ),
        },
    ),
}
