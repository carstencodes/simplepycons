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


class RescuetimeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rescuetime"

    @property
    def original_file_name(self) -> "str":
        return "rescuetime.svg"

    @property
    def title(self) -> "str":
        return "RescueTime"

    @property
    def primary_color(self) -> "str":
        return "#161A3B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RescueTime</title>
     <path d="m24 7.626v8.749c0 .597-.485 1.092-1.091
 1.092h-5.447v5.452c0 .596-.485 1.092-1.091 1.092h-8.742c-.596
 0-1.091-.486-1.091-1.092v-5.452h-5.447c-.596
 0-1.091-.485-1.091-1.092v-8.749c0-.597.485-1.092
 1.091-1.092h5.447v-5.452c0-.596.485-1.092 1.091-1.092h8.742c.596 0
 1.091.485 1.091 1.092v5.452h5.447c.596 0 1.091.495 1.091
 1.092zm-3.325 4.339-2.192-1.649.333
 1.042-4.891-.344c.152.304.243.638.243.992 0
 .343-.081.667-.213.95l4.871-.364-.323 1.022zm-7.579.03-.495-8
 1.021.324-1.647-2.185-1.647 2.195 1.04-.334-.454 8c0 .597.485 1.093
 1.091 1.093.596 0 1.091-.486 1.091-1.093z" />
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
