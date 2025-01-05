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


class LensIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lens"

    @property
    def original_file_name(self) -> "str":
        return "lens.svg"

    @property
    def title(self) -> "str":
        return "Lens"

    @property
    def primary_color(self) -> "str":
        return "#3D90CE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lens</title>
     <path d="M9.255 3.5H3.5v4.255l3.75 4.715ZM3.5
 8.955v7.125h5.665ZM19.545 3.5H10.02L8.87 8.635Zm-.9
 17H20.5v-8.4l-4.32-2.105Zm-5.79-12.95 7.645 3.72v-7.4ZM3.5
 16.825V20.5h6.88l2.875-3.675zm7.83 3.675h6.545l-1.51-6.435zM0
 0h24v24H0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/lensapp/lens/blob/3cc12d95'''

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
