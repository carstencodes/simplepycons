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


class OrcidIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "orcid"

    @property
    def original_file_name(self) -> "str":
        return "orcid.svg"

    @property
    def title(self) -> "str":
        return "ORCID"

    @property
    def primary_color(self) -> "str":
        return "#A6CE39"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ORCID</title>
     <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372
 12-12S18.628 0 12 0zM7.369 4.378c.525 0
 .947.431.947.947s-.422.947-.947.947a.95.95 0 0
 1-.947-.947c0-.525.422-.947.947-.947zm-.722
 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344
 5.025 0 2.578-2.016 5.025-5.325 5.025h-3.919V7.416zm1.444
 1.303v7.444h2.297c3.272 0 4.022-2.484 4.022-3.722
 0-2.016-1.284-3.722-4.097-3.722h-2.222z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://orcid.figshare.com/articles/figure/OR'''

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
