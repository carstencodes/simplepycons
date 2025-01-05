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


class StardockIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stardock"

    @property
    def original_file_name(self) -> "str":
        return "stardock.svg"

    @property
    def title(self) -> "str":
        return "Stardock"

    @property
    def primary_color(self) -> "str":
        return "#004B8D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stardock</title>
     <path d="M22.337 3.28c-.108
 0-.22.007-.336.017-1.553.129-3.886.917-6.557 2.217a7.326 7.326 0 0
 0-3.71-.994c-4.124 0-7.478 3.354-7.478 7.496 0 .674.093 1.33.262
 1.95-3.224 2.697-5.04 5.153-4.385 6.221.712 1.125 3.992.412
 8.115-1.556a7.55 7.55 0 0 0 3.484.863c4.124 0 7.48-3.356 7.48-7.478
 0-.544-.058-1.086-.17-1.592 3.504-2.867 5.529-5.491
 4.816-6.615-.24-.375-.768-.545-1.521-.53Zm-4.324
 1.708c-1.912.769-4.666 1.706-5.64 3.711-.564 1.143.371 2.436.84
 3.035.47.62 1.35 2.174-.13 3.786-1.5 1.63-7.028 3.318-7.028 3.318
 1.78-.843 4.91-2.06
 5.396-4.16.375-1.593-1.142-2.493-1.555-3.205-.412-.712-.842-1.93
 1.313-3.54 2.156-1.631 6.804-2.945 6.804-2.945Zm1.02.758c.67-.007
 1.153.151 1.378.498.43.675-.207 1.95-1.556 3.393a7.514 7.514 0 0
 0-2.323-3.393c.975-.318 1.832-.49 2.502-.498zM4.8 14.79a7.627 7.627 0
 0 0 2.305 3.074c-1.762.525-3.074.524-3.467-.113-.394-.618.075-1.706
 1.162-2.96z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.stardock.com/press/stardock%20bra'''

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
