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


class SecurityscorecardIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "securityscorecard"

    @property
    def original_file_name(self) -> "str":
        return "securityscorecard.svg"

    @property
    def title(self) -> "str":
        return "SecurityScorecard"

    @property
    def primary_color(self) -> "str":
        return "#7033FD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SecurityScorecard</title>
     <path d="M16.3696 2.5006 12.0006 5 7.6303 7.5006v-5L12.0006
 0Zm6.1177 3.499.0028 4.986-8.7282-4.9929 4.3564-2.4923Zm-4.369
 9.5085-.0014 4.9972 4.3774-2.5007-.0028-5.018-4.3732-2.502zM7.6274
 21.502 12.0006 24l4.369-2.4952v-4.9972zM7.6303 9.5v5.0014l4.3703
 2.4992 4.369-2.4937V9.5001l-4.369-2.4993Zm-6.1248 8.5044.0028-5.0055
 8.7464 5.0027-4.376 2.5008Zm4.376-14.504L1.5125 6.001l-.0028 4.9985
 4.3718 2.502z" />
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
