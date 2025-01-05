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


class RimeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rime"

    @property
    def original_file_name(self) -> "str":
        return "rime.svg"

    @property
    def title(self) -> "str":
        return "Rime"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rime</title>
     <path d="M21.733 0H2.267C1 0 0 1 0 2.267v19.466C0 23 1 24 2.267
 24h19.466C23 24 24 23 24 21.733V2.267C24 1 22.933 0 21.733 0Zm-1.6
 20.667H19.8c-.6 0-5.933-.134-7.733-.134-1.934
 0-7.867.134-7.934.134H3.8v-1.134L3.733 18.4h.334c.066 0 4.2-.2
 6.733-.267v-2.466c-2.733-.134-4.667-.867-5.933-2.134-1.934-2-1.8-4.866-1.734-7.933v-.867l2.4.067v.933c-.066
 2.6-.2 4.867 1.067 6.134.8.8 2.133 1.266 4.2
 1.4V3.533h2.4V13.2c2-.133 3.4-.6 4.2-1.4 1.2-1.267 1.133-3.533
 1.067-6.133v-.934l2.4-.066v.866c.133 3.067.2 5.934-1.734 7.934-1.266
 1.266-3.2 2-5.933 2.133v2.467c2.467.066 6.667.266
 6.733.266h.334l-.067 1.134Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rime/home/blob/65738f446c7'''

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
