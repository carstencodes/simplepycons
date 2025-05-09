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


class ExpressIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "express"

    @property
    def original_file_name(self) -> "str":
        return "express.svg"

    @property
    def title(self) -> "str":
        return "Express"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Express</title>
     <path d="M24 18.588a1.529 1.529 0
 01-1.895-.72l-3.45-4.771-.5-.667-4.003 5.444a1.466 1.466 0
 01-1.802.708l5.158-6.92-4.798-6.251a1.595 1.595 0 011.9.666l3.576
 4.83 3.596-4.81a1.435 1.435 0 011.788-.668L21.708 7.9l-2.522
 3.283a.666.666 0 000 .994l4.804 6.412zM.002
 11.576l.42-2.075c1.154-4.103 5.858-5.81 9.094-3.27 1.895 1.489 2.368
 3.597 2.275 5.973H1.116C.943 16.447 4.005 19.009 7.92 17.7a4.078
 4.078 0 002.582-2.876c.207-.666.548-.78 1.174-.588a5.417 5.417 0
 01-2.589 3.957 6.272 6.272 0 01-7.306-.933 6.575 6.575 0
 01-1.64-3.858c0-.235-.08-.455-.134-.666A88.33 88.33 0 010
 11.577zm1.127-.286h9.654c-.06-3.076-2.001-5.258-4.59-5.278-2.882-.04-4.944
 2.094-5.071 5.264z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/openjs-foundation/artwork/
blob/ac43961d1157f973c54f210cf5e0c9c45e3d3f10/projects/express/express'''

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
