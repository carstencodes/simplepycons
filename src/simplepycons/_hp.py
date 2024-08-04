#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class HpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hp"

    @property
    def original_file_name(self) -> "str":
        return "hp.svg"

    @property
    def title(self) -> "str":
        return "HP"

    @property
    def primary_color(self) -> "str":
        return "#0096D6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HP</title>
     <path d="M12.0069 24h-.3572l2.459-6.7453h3.3796c.5907 0
 1.2364-.4533
 1.4424-1.0166l2.6652-7.3085c.4396-1.1952-.2473-2.1706-1.525-2.1706h-4.6983l-3.929
 10.798-2.2255 6.127C3.929 22.434 0 17.6806 0 12.007 0 6.498 3.7092
 1.8546 8.7647.4396L6.4705 6.759 2.6514 17.2547h2.5415L8.4488
 8.339h1.9095l-3.2558
 8.9158H9.644l3.0223-8.3251c.4396-1.1952-.2473-2.1706-1.525-2.1706h-2.143l2.459-6.7453C11.636
 0 11.8145 0 11.9931 0 18.6285 0 24 5.3715 24 12.007c.0137
 6.6216-5.3578 11.993-11.9931 11.993zM19.2742 8.325h-1.9096l-2.6789
 7.336h1.9096l2.6789-7.336z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://brandcentral.hp.com/us/en/elements/hp'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://brandcentral.hp.com/us/en/elements/hp'''

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