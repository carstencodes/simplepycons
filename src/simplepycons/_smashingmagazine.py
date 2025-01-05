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


class SmashingMagazineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "smashingmagazine"

    @property
    def original_file_name(self) -> "str":
        return "smashingmagazine.svg"

    @property
    def title(self) -> "str":
        return "Smashing Magazine"

    @property
    def primary_color(self) -> "str":
        return "#E85C33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Smashing Magazine</title>
     <path d="M7.734 12.002c.766.524 1.662 1.01 2.708 1.443 1.785.742
 2.985 1.387 3.601 1.936.615.547.928 1.248.928 2.104-.005 1.457-1.023
 2.189-3.076 2.189-1.977 0-3.75-.627-5.326-1.875l-1.871
 4.186c1.422.761 2.58 1.257 3.475
 1.496l.141.033-1.798.416c-1.271.292-2.539-.503-2.832-1.771L.061
 6.5c-.291-1.271.5-2.539
 1.773-2.835l4.375-1.009c-.158.155-.307.316-.441.485l-.018.021c-.753.949-1.131
 2.115-1.131 3.505 0 2.101 1.03 3.87 3.079
 5.296l.046.029-.01.01zm10.358.072c-.84-.672-1.904-1.268-3.24-1.786-1.98-.784-3.271-1.41-3.871-1.872-.6-.465-.914-.981-.914-1.557
 0-1.459.914-2.19 2.76-2.19 2.041 0 3.646.494 4.786
 1.476l1.515-4.08c-1.095-.556-2.235-.96-3.405-1.216l-.06-.015c-.256-.061-.525-.12-.811-.164l2.625-.602c1.275-.285
 2.535.511 2.836 1.771l3.63 15.647c.284 1.274-.51 2.551-1.784
 2.835l-2.985.69c.824-1.051 1.245-2.34 1.245-3.87
 0-1.575-.437-2.911-1.306-4.021-.285-.346-.615-.676-1.006-1.006l-.044-.029.029-.011z"
 />
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
