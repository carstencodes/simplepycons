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


class SnowflakeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "snowflake"

    @property
    def original_file_name(self) -> "str":
        return "snowflake.svg"

    @property
    def title(self) -> "str":
        return "Snowflake"

    @property
    def primary_color(self) -> "str":
        return "#29B5E8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Snowflake</title>
     <path d="M24 3.459c0 .646-.418 1.18-1.141 1.18-.723
 0-1.142-.534-1.142-1.18 0-.647.419-1.18 1.142-1.18.723 0 1.141.533
 1.141 1.18zm-.228 0c0-.533-.38-.951-.913-.951s-.913.38-.913.95c0
 .533.38.952.913.952.57 0 .913-.419.913-.951zm-1.37-.533h.495c.266 0
 .456.152.456.38 0
 .153-.076.229-.19.305l.19.266v.038h-.266l-.19-.266h-.229v.266h-.266zm.495.228h-.229v.267h.229c.114
 0 .152-.038.152-.114.038-.077-.038-.153-.152-.153zM7.602
 12.4c.038-.151.076-.304.076-.456
 0-.114-.038-.228-.038-.342-.114-.343-.304-.647-.646-.838l-4.87-2.777c-.685-.38-1.56-.152-1.94.533-.381.685-.153
 1.56.532 1.94l2.701 1.56-2.701 1.56c-.685.38-.913 1.256-.533
 1.94.38.685 1.256.914
 1.94.533l4.832-2.777c.343-.267.571-.533.647-.876zm1.332
 2.626c-.266-.038-.57.038-.837.19l-4.832 2.777c-.685.38-.913
 1.256-.532 1.94.38.686 1.255.914 1.94.533l2.701-1.56v3.12c0 .8.647
 1.408 1.446 1.408.799 0 1.407-.647
 1.407-1.408v-5.592c0-.761-.57-1.37-1.293-1.408zm4.946-6.088c.266.038.57-.038.837-.19l4.832-2.777c.685-.38.913-1.256.532-1.94-.38-.686-1.255-.914-1.94-.533l-2.701
 1.56V1.975c0-.799-.647-1.408-1.446-1.408-.799 0-1.446.609-1.446
 1.408V7.53c0 .76.609 1.37 1.332 1.407zM3.265 5.97l4.832
 2.777c.266.152.533.19.837.19.723-.038 1.331-.684
 1.331-1.407V1.975c0-.799-.646-1.408-1.407-1.408-.799
 0-1.446.647-1.446
 1.408v3.12l-2.701-1.56c-.685-.38-1.56-.152-1.94.533-.419.646-.19
 1.521.494 1.902zm9.093 6.011a.412.412 0
 00-.114-.266l-.57-.571a.346.346 0 00-.267-.114.412.412 0
 00-.266.114l-.571.57a.411.411 0 00-.114.267c0
 .076.038.19.114.267l.57.57a.345.345 0 00.267.114c.076 0
 .19-.038.266-.114l.571-.57a.412.412 0 00.114-.267zm1.598.533L11.94
 14.53c-.039.038-.153.114-.229.114h-.608a.411.411 0 01-.267-.114L8.82
 12.514a.408.408 0
 01-.076-.229v-.608c0-.076.038-.19.114-.267l2.016-2.016a.41.41 0
 01.267-.114h.608a.41.41 0 01.267.114l2.016 2.016a.347.347 0
 01.114.267v.608c-.076.077-.114.19-.19.229zm5.593
 5.44l-4.832-2.777c-.266-.152-.57-.19-.837-.152-.723.038-1.332.684-1.332
 1.408v5.554c0 .8.647 1.408 1.408 1.408.799 0 1.446-.647
 1.446-1.408v-3.12l2.7 1.56c.686.38 1.561.152
 1.941-.533.419-.646.19-1.521-.494-1.94zm2.549-7.533l-2.701 1.56 2.7
 1.56c.686.38.914 1.256.533
 1.94-.38.685-1.255.913-1.94.533l-4.832-2.778a1.644 1.644 0
 01-.647-.798c-.037-.153-.076-.305-.076-.457
 0-.114.039-.228.039-.342.114-.343.342-.647.646-.837l4.832-2.778c.685-.38
 1.56-.152 1.94.533.457.609.19 1.484-.494 1.864" />
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
