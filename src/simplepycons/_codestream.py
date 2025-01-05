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


class CodestreamIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codestream"

    @property
    def original_file_name(self) -> "str":
        return "codestream.svg"

    @property
    def title(self) -> "str":
        return "CodeStream"

    @property
    def primary_color(self) -> "str":
        return "#008C99"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CodeStream</title>
     <path d="M10.5408 18.2457a6.4596 6.4596 0 0 1
 0-12.5804V1.2199A.4315.4315 0 0 0 9.795.9261l-9.36 9.9713a1.61 1.61 0
 0 0 0 2.2011l9.36 9.9754a.4315.4315 0 0 0 .7463-.2954zm2.9184
 0a6.4596 6.4596 0 0 0 0-12.5804V1.2199a.4315.4315 0 0 1
 .7463-.2938l9.3596 9.9713a1.61 1.61 0 0 1 0 2.2011l-9.3596
 9.9754a.4315.4315 0 0 1-.7463-.2954zm2.2636-6.2902a3.7276 3.7307 0 0
 1-3.7277 3.7307 3.7276 3.7307 0 0 1-3.7276-3.7307 3.7276 3.7307 0 0 1
 3.7276-3.7307 3.7276 3.7307 0 0 1 3.7277 3.7307z" />
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
