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


class AstraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "astra"

    @property
    def original_file_name(self) -> "str":
        return "astra.svg"

    @property
    def title(self) -> "str":
        return "Astra"

    @property
    def primary_color(self) -> "str":
        return "#5C2EDE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Astra</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0m-.1452 5.3226 1.4517 2.9032c-1.6452
 3.3194-3.2904 6.6484-4.9355 9.9677H5.758c2.0323-4.287 4.0646-8.5838
 6.0968-12.871m2.7097 5.3226c1.229 2.516 2.4484 5.0322 3.6774
 7.5483h-2.8064c-.3194-.7451-.6484-1.4806-.9678-2.2258H12l.0484-.0967c.842-1.742
 1.6742-3.4839 2.5161-5.2258" />
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
