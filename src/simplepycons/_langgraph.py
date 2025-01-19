#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class LanggraphIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "langgraph"

    @property
    def original_file_name(self) -> "str":
        return "langgraph.svg"

    @property
    def title(self) -> "str":
        return "LangGraph"

    @property
    def primary_color(self) -> "str":
        return "#1C3C3C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LangGraph</title>
     <path d="M6.099 5.88H17.9C21.264 5.88 24 8.625 24 12s-2.736
 6.12-6.099 6.12H6.1C2.736 18.12 0 15.375 0 12s2.736-6.12
 6.099-6.12Zm5.419
 9.487c.148.156.367.148.561.108h.002c.09-.073-.038-.166-.16-.254-.074-.054-.145-.105-.166-.15.068-.083-.132-.27-.289-.417a1.539
 1.539 0 0 1-.15-.151c-.11-.12-.155-.273-.2-.427a1.575 1.575 0 0
 0-.11-.297c-.304-.708-.653-1.41-1.143-2.01-.315-.398-.674-.755-1.033-1.112-.232-.23-.463-.46-.683-.701-.226-.234-.362-.521-.499-.81-.114-.24-.228-.482-.396-.693-.507-.75-2.107-.955-2.342.105
 0
 .033-.01.054-.039.075-.13.095-.245.203-.342.334-.238.332-.274.895.022
 1.193l.001-.02c.01-.15.02-.29.139-.399.228.198.576.268.841.12.32.46.422
 1.015.525 1.572.085.464.17.93.382
 1.341l.014.022c.124.208.25.419.41.6.059.09.178.187.297.284.157.128.314.256.329.366v.146c-.001.29-.002.59.184.83.103.208-.15.418-.352.392a.989.989
 0 0
 1-.354-.043c-.165-.04-.329-.08-.462-.003-.038.04-.091.042-.145.043-.064.002-.129.004-.167.07a.29.29
 0 0
 1-.045.066c-.042.051-.087.107-.033.149l.015-.011c.082-.063.16-.123.27-.085-.014.082.039.103.092.125l.027.012a.357.357
 0 0 1-.008.057c-.009.046-.017.09.018.13a.605.605 0 0 0
 .046-.056c.037-.046.073-.094.139-.11.144.192.289.112.471.012.206-.114.459-.253.81-.056-.135-.007-.255.01-.345.121-.023.025-.042.054-.002.087.207-.135.294-.086.375-.04.06.032.115.063.212.024l.07-.037c.155-.084.314-.17.499-.14-.139.04-.188.127-.242.223-.026.047-.054.097-.094.143-.021.021-.03.046-.007.082.29-.024.4-.098.548-.197.07-.047.15-.1.261-.157.124-.076.248-.028.368.02.13.05.255.1.371-.013.037-.035.083-.035.129-.036.016
 0 .033 0
 .05-.002-.037-.194-.24-.191-.448-.189-.24.003-.483.005-.475-.295.222-.152.224-.415.226-.665
 0-.06
 0-.119.005-.176.163.092.336.163.508.234.162.066.323.133.474.215.157.254.404.59.732.568.008-.026.016-.048.026-.074.019.003.039.008.059.014.086.021.178.045.223-.057zm6.429-2.886a1.014
 1.014 0 0 0 1.729-.715 1.01 1.01 0 0 0-1.013-1.01c-.126
 0-.25.023-.364.068l-.58-.848-.405.278.583.851a1.009 1.009 0 0 0 .05
 1.376zm-1.818-2.744a1.014 1.014 0 0 0 1.42-.615 1.008 1.008 0 0
 0-.845-1.293 1.015 1.015 0 0 0-1.095.712 1.008 1.008 0 0 0 .52
 1.196zm0 5.867a1.015 1.015 0 0 0 1.42-.615 1.008 1.008 0 0
 0-.845-1.293 1.015 1.015 0 0 0-1.095.712 1.008 1.008 0 0 0 .52
 1.196zm.932-3.586v-.503h-1.55a1.003 1.003 0 0
 0-.218-.412l.583-.864-.424-.28-.583.863a1.014 1.014 0 0
 0-.333-.06c-.268 0-.525.106-.714.294a1.002 1.002 0 0 0 1.047
 1.655l.583.864.42-.281-.579-.864c.104-.119.178-.26.217-.412z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
