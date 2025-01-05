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


class KeeperIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keeper"

    @property
    def original_file_name(self) -> "str":
        return "keeper.svg"

    @property
    def title(self) -> "str":
        return "Keeper"

    @property
    def primary_color(self) -> "str":
        return "#FFC700"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Keeper</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm1.365 1.788 1.854.472v2.597l2.073-1.704 1.537
 1.135-3.949 3.247-1.515-.008zm-9.067 15.54L2.445 15.75V8.7L4.298
 7zm3.631 2.22L6.076 21.16V3l1.853 1.614zm9.363
 1.555-2.073-1.705v2.597l-1.854.473v-5.74l1.515-.007 3.95
 3.246zm2.733-2.473-4.604-3.674h-3.826v7.512H9.742v-9.365h6.329l5.11
 4.078zm2.62-8.329-2.059 1.7 2.059 1.698-1.181 1.431L17.67
 12l3.793-3.13zm-6.574.6H9.742V1.534h1.853v7.512h3.826l4.604-3.674
 1.156 1.449z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.keepersecurity.com/assets/pdf/bra'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://docs.keeper.io/en/sso-connect-cloud/g'''

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
