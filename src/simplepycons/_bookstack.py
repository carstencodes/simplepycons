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


class BookstackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bookstack"

    @property
    def original_file_name(self) -> "str":
        return "bookstack.svg"

    @property
    def title(self) -> "str":
        return "BookStack"

    @property
    def primary_color(self) -> "str":
        return "#0288D1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BookStack</title>
     <path d="M.3013
 17.6146c-.1299-.3387-.5228-1.5119-.1337-2.4314l9.8273 5.6738a.329.329
 0 0 0 .3299 0L24 12.9616v2.3542l-13.8401 7.9906-9.8586-5.6918zM.1911
 8.9628c-.2882.8769.0149 2.0581.1236 2.4261l9.8452 5.6841L24
 9.0823V6.7275L10.3248 14.623a.329.329 0 0 1-.3299 0L.1911
 8.9628zm13.1698-1.9361c-.1819.1113-.4394.0015-.4852-.2064l-.2805-1.1336-2.1254-.1752a.33.33
 0 0 1-.1378-.6145l5.5782-3.2207-1.7021-.9826L.6979 8.4935l9.462 5.463
 13.5104-7.8004-4.401-2.5407-5.9084 3.4113zm-.1821-1.7286.2321.938
 5.1984-3.0014-2.0395-1.1775-4.994 2.8834 1.3099.108a.3302.3302 0 0 1
 .2931.2495zM24 9.845l-13.6752 7.8954a.329.329 0 0 1-.3299 0L.1678
 12.0667c-.3891.919.003 2.0914.1332 2.4311l9.8589 5.692L24
 12.1993V9.845z" />
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
