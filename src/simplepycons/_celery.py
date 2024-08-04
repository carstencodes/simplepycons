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


class CeleryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "celery"

    @property
    def original_file_name(self) -> "str":
        return "celery.svg"

    @property
    def title(self) -> "str":
        return "Celery"

    @property
    def primary_color(self) -> "str":
        return "#37814A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Celery</title>
     <path d="M2.303 0A2.298 2.298 0 0 0 0 2.303v19.394A2.298 2.298 0
 0 0 2.303 24h19.394A2.298 2.298 0 0 0 24 21.697V2.303A2.298 2.298 0 0
 0 21.697 0zm8.177 3.072c4.098 0 7.028 1.438 7.68 1.764l-1.194
 2.55c-2.442-1.057-4.993-1.41-5.672-1.41-1.574 0-2.17.922-2.17
 1.763v8.494c0 .869.596 1.791 2.17 1.791.679 0 3.23-.38
 5.672-1.41l1.194 2.496c-.435.271-3.637 1.818-7.68 1.818-1.112
 0-4.64-.244-4.64-4.64V7.713c0-4.397 3.528-4.64 4.64-4.64z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/celery/celery/blob/4d77ddd'''

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