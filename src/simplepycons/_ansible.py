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


class AnsibleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ansible"

    @property
    def original_file_name(self) -> "str":
        return "ansible.svg"

    @property
    def title(self) -> "str":
        return "Ansible"

    @property
    def primary_color(self) -> "str":
        return "#EE0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ansible</title>
     <path d="M10.617 11.473l4.686 3.695-3.102-7.662zM12 0C5.371 0 0
 5.371 0 12s5.371 12 12 12 12-5.371 12-12S18.629 0 12 0zm5.797
 17.305c-.011.471-.403.842-.875.83-.236
 0-.416-.09-.664-.293l-6.19-5-2.079 5.203H6.191L11.438
 5.44c.124-.314.427-.52.764-.506.326-.014.63.189.742.506l4.774
 11.494c.045.111.08.234.08.348-.001.009-.001.009-.001.023z" />
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
