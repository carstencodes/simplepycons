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


class FreelancerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freelancer"

    @property
    def original_file_name(self) -> "str":
        return "freelancer.svg"

    @property
    def title(self) -> "str":
        return "Freelancer"

    @property
    def primary_color(self) -> "str":
        return "#29B2FE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Freelancer</title>
     <path d="M14.096 3.076l1.634 2.292L24 3.076M5.503
 20.924l4.474-4.374-2.692-2.89m6.133-10.584L11.027 5.23l4.022.15M4.124
 3.077l.857 1.76 4.734.294m-3.058 7.072l3.497-6.522L0 5.13m7.064
 7.485l3.303 3.548 3.643-3.57 1.13-6.652-4.439-.228Z" />
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
