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


class CrewaiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "crewai"

    @property
    def original_file_name(self) -> "str":
        return "crewai.svg"

    @property
    def title(self) -> "str":
        return "CrewAI"

    @property
    def primary_color(self) -> "str":
        return "#FF5A50"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CrewAI</title>
     <path d="M12.482.18C7.161 1.319 1.478 9.069 1.426 15.372c-.051
 5.527 3.1 8.68 8.68 8.627 6.716-.05 14.259-6.87
 12.09-10.9-.672-1.292-1.396-1.344-2.687-.207-1.602
 1.395-1.654.31-.207-2.893 1.757-3.98 1.705-5.322-.31-7.544C17.03.388
 14.962-.388 12.482.181Zm5.322 2.068c2.273 2.015 2.376 4.236.465
 8.42-1.395 3.1-2.17 3.515-3.824 1.86-1.24-1.24-1.343-3.46-.258-6.044
 1.137-2.635.982-3.1-.568-1.653-3.72 3.358-6.458 9.765-5.424
 12.503.464 1.189.825 1.395 2.737 1.395 2.79 0 6.303-1.705 7.957-3.926
 1.756-2.274 2.79-2.274 2.79-.052 0 3.875-6.459 8.627-11.625
 8.627-6.251 0-9.351-4.752-7.491-11.47.878-2.995 4.443-7.904
 7.077-9.66 3.255-2.17 5.684-2.17 8.164 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/crewAIInc/crewAI/blob/a769'''

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
