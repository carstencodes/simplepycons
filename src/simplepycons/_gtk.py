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


class GtkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gtk"

    @property
    def original_file_name(self) -> "str":
        return "gtk.svg"

    @property
    def title(self) -> "str":
        return "GTK"

    @property
    def primary_color(self) -> "str":
        return "#7FE719"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GTK</title>
     <path d="M9.01 23.773V14.45l-7.584 2.245Zm0-13.87L.91 3.828l.502
 12.526 7.597-2.249ZM9.57 24l12.353-5.146-8.285-5.775-4.068
 1.204ZM23.09 5.815l-9.257 2.849v4.148l8.237 5.741ZM9.57
 9.975v3.964l3.932-1.164v-4.01Zm-.228-.52 4.16-1.28V0L1.231
 3.37ZM22.715 5.34 13.833.052v8.021Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://foundation.gnome.org/logo-and-tradema'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:GTK_l'''

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
