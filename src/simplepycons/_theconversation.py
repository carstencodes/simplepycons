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


class TheConversationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "theconversation"

    @property
    def original_file_name(self) -> "str":
        return "theconversation.svg"

    @property
    def title(self) -> "str":
        return "The Conversation"

    @property
    def primary_color(self) -> "str":
        return "#D8352A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The Conversation</title>
     <path d="M23.996
 10.543c-.131-4.91-4.289-8.773-9.2-8.773H9.005a8.997 8.997 0 0 0-5.957
 15.746L1.05 22.23l4.942-2.98c.95.36 1.964.524 3.012.524h6.024c5.04 0
 9.099-4.156 8.969-9.23zm-8.937 5.958H9.07c-2.587
 0-5.205-2.03-5.696-4.583a5.724 5.724 0 0 1 5.63-6.874h5.99c2.586 0
 5.205 2.03 5.696 4.582.688 3.667-2.095 6.875-5.63 6.875z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://theconversation.com/republishing-guid'''

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
