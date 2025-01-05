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


class CapacitorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "capacitor"

    @property
    def original_file_name(self) -> "str":
        return "capacitor.svg"

    @property
    def title(self) -> "str":
        return "Capacitor"

    @property
    def primary_color(self) -> "str":
        return "#119EFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Capacitor</title>
     <path d="M24 3.7l-5.766 5.766 5.725 5.736-3.713 3.712L5.073 3.742
 8.786.03l5.736 5.726L20.284 0 24 3.7zM.029 8.785l3.713-3.713 15.173
 15.173-3.713 3.714-5.732-5.726L3.7 24 0 20.285l5.754-5.764L.029
 8.785z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ionic-team/ionicons-site/b
lob/b0c97018d737b763301154231b34e1b882c0c84d/docs/ionicons/svg/logo-ca'''

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
