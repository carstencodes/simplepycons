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


class CommonWorkflowLanguageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "commonworkflowlanguage"

    @property
    def original_file_name(self) -> "str":
        return "commonworkflowlanguage.svg"

    @property
    def title(self) -> "str":
        return "Common Workflow Language"

    @property
    def primary_color(self) -> "str":
        return "#B5314C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Common Workflow Language</title>
     <path d="M13.905 0L8.571 5.4l.037.037.096.096 3.586 3.395-2.24
 2.252h-.01l-1.576 1.586 3.737 3.766-3.735 3.803.126.139v.012L12.052
 24l1.608-1.64-1.98-2.034 3.737-3.79-1.608-1.642-.01.012-2.13-2.129
 3.867-3.866-.017-.015.016-.016-3.641-3.524 3.64-3.694z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/common-workflow-language/l'''

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
