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


class AkamaiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "akamai"

    @property
    def original_file_name(self) -> "str":
        return "akamai.svg"

    @property
    def title(self) -> "str":
        return "Akamai"

    @property
    def primary_color(self) -> "str":
        return "#0096D6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Akamai</title>
     <path d="M13.0548 0C6.384 0 .961 5.3802.961 12.0078.961 18.6354
 6.3698 24 13.0548 24c.6168 0
 .6454-.3572.0859-.5293-4.9349-1.5063-8.5352-6.069-8.5352-11.4629
 0-5.4656 3.6725-10.0706 8.6934-11.5195C13.8153.3448 13.6716 0 13.0548
 0Zm2.3242 1.8223c-5.2648 0-9.5254 4.2606-9.5254 9.5254 0 1.2193.2285
 2.3818.6445
 3.4433.1722.459.4454.4584.4024.0137-.0287-.3156-.0567-.6447-.0567-.9746
 0-5.2648 4.2606-9.5254 9.5254-9.5254 4.9779 0 6.4698 2.2235 6.6563
 2.08.2008-.1577-1.808-4.5624-7.6465-4.5624zm.4687
 4.0703c-1.8622.0592-3.651.7168-5.1035
 1.8554-.2582.2009-.1567.3284.1445.1993 2.4675-1.076 5.5812-1.1046
 8.6368-.043 2.0514.7173 3.2413 1.7364 3.3418
 1.6934.1578-.0718-1.1915-2.2226-3.6446-3.1407-1.1135-.4196-2.2576-.6-3.375-.5644z"
 />
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
