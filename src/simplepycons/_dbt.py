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


class DbtIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dbt"

    @property
    def original_file_name(self) -> "str":
        return "dbt.svg"

    @property
    def title(self) -> "str":
        return "dbt"

    @property
    def primary_color(self) -> "str":
        return "#FF694B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>dbt</title>
     <path d="M17.9004 9.3763a8.1488 8.1488 0 0
 0-3.0421-3.1206l1.7708.8385a10.2874 10.2874 0 0 1 3.74
 3.0007l3.234-5.9295a2.8546 2.8546 0 0 0-.0611-2.9604C22.7566.0371
 21.2112-.3409 19.9754.3327l-5.8749 3.2101a4.3612 4.3612 0 0 1-4.1761
 0L4.1769.408a2.8545 2.8545 0 0 0-2.9592.0632c-1.1673.7853-1.5452
 2.33-.8723 3.5655L3.55 9.9106a4.3612 4.3612 0 0 1 0 4.1772l-3.1272
 5.743a2.86 2.86 0 0 0 .085 2.9974c.794 1.1438 2.3225 1.5054
 3.5448.8385l6.0581-3.3049a10.2877 10.2877 0 0
 1-3.0051-3.7454l-.8374-1.7708a8.148 8.148 0 0 0 3.1206 3.0421l10.5832
 5.779c1.2213.666 2.7481.3055 3.5426-.8363a2.8699 2.8699 0 0 0
 .0796-3.0018L17.9004 9.3763zm3.3801-7.7351c.6022 0 1.0904.4882 1.0904
 1.0904s-.4882 1.0904-1.0904
 1.0904-1.0904-.4882-1.0904-1.0904.4882-1.0904 1.0904-1.0904zM2.7442
 3.822c-.6022 0-1.0904-.4882-1.0904-1.0904s.4882-1.0904 1.0904-1.0904
 1.0904.4882 1.0904 1.0904S3.3464 3.822 2.7442 3.822zm0 18.5363c-.6022
 0-1.0904-.4882-1.0904-1.0904 0-.6022.4882-1.0904
 1.0904-1.0904s1.0904.4882 1.0904 1.0904c0 .6022-.4882 1.0904-1.0904
 1.0904zm10.3585-11.4489c-1.2008-.0035-2.177.9672-2.1805 2.1679a2.1738
 2.1738 0 0 0 .7052
 1.6091c-1.4872-.2091-2.5234-1.5843-2.3142-3.0716.2091-1.4872
 1.5843-2.5234 3.0716-2.3142a2.7194 2.7194 0 0 1 2.3142 2.3142 2.1623
 2.1623 0 0 0-1.5963-.7054zm8.1778 11.4489c-.6022
 0-1.0904-.4882-1.0904-1.0904 0-.6022.4882-1.0904
 1.0904-1.0904s1.0904.4882 1.0904 1.0904c0 .6022-.4882 1.0904-1.0904
 1.0904z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/fishtown-analytics/dbt-sty
leguide/blob/a2895e005457eda531880dfde62f31959d42f18b/_includes/icons/'''

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
