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


class SSevenAirlinesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "s7airlines"

    @property
    def original_file_name(self) -> "str":
        return "s7airlines.svg"

    @property
    def title(self) -> "str":
        return "S7 Airlines"

    @property
    def primary_color(self) -> "str":
        return "#C4D600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>S7 Airlines</title>
     <path d="M12.004 0C5.375 0 0 5.373 0 12.002 0 18.632 5.375 24
 12.004 24 18.63 24 24 18.632 24 12.002 24 5.373 18.631 0 12.004
 0zm-.875 5.739h1.705L12 7.825h-1.168c-1.255
 0-2.061.004-2.496.148-.423.132-.735.29-.906.54-.157.202-.21.477-.21.716
 0 .25.027.487.275.806.305.305.809.699 1.797 1.307 1.97 1.229 2.552
 2.204 2.552 3.487 0 2.09-1.97 4.084-5.272 4.084-.992
 0-2.377-.146-2.961-.332l-.307-.09c.12-.397.512-1.493.685-1.956l.31.078c.648.16
 1.664.252 2.338.252 1.932 0 2.682-.872 2.682-1.638
 0-.7-.382-1.084-2.299-2.246-1.796-1.11-2.417-2.076-2.417-3.409 0-1.6
 1.03-2.818 2.522-3.399.888-.33 2.114-.434 4.004-.434zm2.959
 0h5.871c.276 0 .329.195.223.407-.384.952-4.007 10.028-4.007
 10.028h-2.421s2.861-7.291 3.336-8.377c-.33
 0-.581.028-1.89.028h-1.947Z" />
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
